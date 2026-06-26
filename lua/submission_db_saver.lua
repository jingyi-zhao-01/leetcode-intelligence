---@diagnostic disable: undefined-global
-- Lua wrapper to save submissions to database
-- Uses TCP connection to submission_server.py for both timer and submission operations


local M = {}
local shown_mem0_recall_at = {}

local function debug_log(msg)
  vim.schedule(function()
    vim.fn.histadd("message", "[submission_db_saver] " .. msg)
  end)
end

local function send_request(request, handlers)
  local uv = vim.loop
  local client = uv.new_tcp()
  local timer = uv.new_timer()
  local closed = false
  local stdout_chunks = {}
  local response_complete = false
  local timeout_ms = handlers.timeout_ms or 5000

  local function close_client()
    if closed then
      return
    end
    closed = true

    if timer and not timer:is_closing() then
      timer:stop()
      timer:close()
    end

    if client and not client:is_closing() then
      client:close()
    end
  end

  local function emit_stdout()
    if handlers.on_stdout and #stdout_chunks > 0 then
      local payload = table.concat(stdout_chunks)
      debug_log("stdout payload: " .. payload:gsub("%s+$", ""))
      handlers.on_stdout(nil, vim.split(payload, "\n", { plain = true }), nil)
    end
  end

  local function finish(exit_code, stderr_msg)
    if stderr_msg and handlers.on_stderr then
      handlers.on_stderr(nil, { stderr_msg }, nil)
    end

    emit_stdout()
    close_client()

    if handlers.on_exit then
      debug_log("finish exit_code=" .. tostring(exit_code))
      handlers.on_exit(nil, exit_code, nil)
    end
  end

  local function maybe_finish_from_chunk(chunk)
    if response_complete then
      return
    end

    local payload = table.concat(stdout_chunks)
    if payload:find("\n", 1, true) then
      response_complete = true
      debug_log("complete response line received")
      vim.schedule(function()
        finish(0)
      end)
    end
  end

  debug_log("connecting to 127.0.0.1:3000 with request " .. request:gsub("%s+$", ""))
  client:connect("127.0.0.1", 3000, function(connect_err)
    if connect_err then
      return vim.schedule(function()
        finish(1, "TCP connect error: " .. tostring(connect_err))
      end)
    end

    debug_log("tcp connected")
    timer:start(timeout_ms, 0, function()
      vim.schedule(function()
        finish(1, "TCP request timed out waiting for response after " .. tostring(timeout_ms) .. "ms")
      end)
    end)

    client:read_start(function(read_err, chunk)
      if read_err then
        return vim.schedule(function()
          finish(1, "TCP read error: " .. tostring(read_err))
        end)
      end

      if chunk then
        debug_log("received chunk bytes=" .. tostring(#chunk))
        table.insert(stdout_chunks, chunk)
        maybe_finish_from_chunk(chunk)
        return
      end

      vim.schedule(function()
        debug_log("tcp eof received")
        finish(0)
      end)
    end)

    client:write(request, function(write_err)
      if write_err then
        return vim.schedule(function()
          finish(1, "TCP write error: " .. tostring(write_err))
        end)
      end

      debug_log("request written, waiting for response line")
    end)
  end)
end

local function json_request(payload)
  return vim.fn.json_encode(payload) .. "\n"
end

local function extract_response_line(data)
  if not data or #data == 0 then
    return nil
  end

  for i = #data, 1, -1 do
    local line = data[i]
    if line and line ~= "" then
      return line
    end
  end
end

local function question_description_text(question)
  if question.description and question.description.bufnr and vim.api.nvim_buf_is_valid(question.description.bufnr) then
    return table.concat(vim.api.nvim_buf_get_lines(question.description.bufnr, 0, -1, false), "\n")
  end

  return question.q and (question.q.translated_content or question.q.content) or ""
end

local function analysis_filetype(question)
  if question and question.bufnr and vim.api.nvim_buf_is_valid(question.bufnr) then
    local ft = vim.bo[question.bufnr].filetype
    if ft and ft ~= "" then
      return ft
    end
  end

  return "text"
end

local function question_topic_tags(question)
  local tags = {}
  local topic_tags = question and question.q and question.q.topic_tags or {}
  if type(topic_tags) ~= "table" then
    return tags
  end

  for _, tag in ipairs(topic_tags) do
    local value = (type(tag) == "table" and (tag.name or tag.slug)) or tag
    if type(value) == "string" and value ~= "" then
      table.insert(tags, value)
    end
  end

  return tags
end

function M.save_submission(question, buffer, item)
  -- Save submission to database via TCP server.
  -- 
  -- Args:
  --   question: Question object with q.title_slug field
  --   buffer: Submission code content
  --   item: Full judge result item object containing status_msg and other fields
  
  local title_slug = question.q.title_slug
  local ai_assist_enabled = false
  if question and type(question.is_auto_ai_assist_enabled) == "function" then
    ai_assist_enabled = question:is_auto_ai_assist_enabled()
  end
  
  -- Convert buffer to string (handle both array of lines and string)
  local content
  if type(buffer) == "table" then
    content = table.concat(buffer, "\n")
  else
    content = buffer or ""
  end

  -- Build JSON request
  local submission_item = type(item) == "table" and vim.deepcopy(item) or {}
  submission_item.lcnvim_ai_assist = ai_assist_enabled

  local request = json_request({
    action = "save_submission",
    title_slug = title_slug,
    content = content,
    item = submission_item
  })
  
  send_request(request, {
    on_exit = function(_, exit_code, _)
      if exit_code == 0 then
        vim.notify("💾 Submission saved to database", vim.log.levels.INFO)
      else
        vim.notify("⚠️  Submission save failed (code: " .. exit_code .. ")", vim.log.levels.WARN)
      end
    end,
    on_stdout = function(_, data, _)
      if data and #data > 0 then
        for _, line in ipairs(data) do
          if line ~= "" then
            vim.notify("Save response: " .. line, vim.log.levels.DEBUG)
          end
        end
      end
    end,
    on_stderr = function(_, data, _)
      if data and #data > 0 then
        for _, line in ipairs(data) do
          if line ~= "" and not line:match("^$") then
            vim.notify("Save error: " .. line, vim.log.levels.ERROR)
          end
        end
      end
    end,
  })
end

function M.timer_start(question)
  -- Drop any existing session and start a fresh timer for the given problem.
  -- This is an explicit user action (Leet session start) that always resets the clock.
  --
  -- Args:
  --   question: Question object with q.title_slug field

  local title_slug = question.q.title_slug

  local request = json_request({
    action = "start_timer",
    title_slug = title_slug
    -- allow_multiple defaults to False on the server side,
    -- so all existing timers are cleared and a fresh one is started.
  })

  send_request(request, {
    on_exit = function(_, exit_code, _)
      if exit_code == 0 then
        vim.notify("⏱️  Session started: " .. title_slug, vim.log.levels.INFO)
      else
        vim.notify("⚠️  Session start failed (code: " .. exit_code .. ")", vim.log.levels.WARN)
      end
    end,
    on_stdout = function(_, data, _)
      if data and #data > 0 then
        for _, line in ipairs(data) do
          if line ~= "" then
            vim.notify("Session response: " .. line, vim.log.levels.DEBUG)
          end
        end
      end
    end,
    on_stderr = function(_, data, _)
      if data and #data > 0 then
        for _, line in ipairs(data) do
          if line ~= "" and not line:match("^$") then
            vim.notify("Session error: " .. line, vim.log.levels.ERROR)
          end
        end
      end
    end,
  })
end

function M.drop_session(question)
  -- Drop any in-memory timer for the given problem without saving a session
  -- record to the database. Called when a question window is unmounted.

  local title_slug = question.q.title_slug

  local request = json_request({
    action = "drop_timer",
    title_slug = title_slug,
  })

  send_request(request, {
    on_exit = function(_, exit_code, _)
      if exit_code ~= 0 then
        vim.notify("⚠️  Session drop failed (code: " .. exit_code .. ")", vim.log.levels.WARN)
      end
    end,
    on_stderr = function(_, data, _)
      if data and #data > 0 then
        for _, line in ipairs(data) do
          if line ~= "" and not line:match("^$") then
            vim.notify("Session drop error: " .. line, vim.log.levels.ERROR)
          end
        end
      end
    end,
  })
end

function M.list_past_submissions(title_slug, submissions)
  if not submissions or vim.tbl_isempty(submissions) then
    vim.notify("No past submissions found for " .. title_slug, vim.log.levels.INFO)
    return
  end

  local lines = {}
  for index, submission in ipairs(submissions) do
    local submitted_at = submission.submitted_at_pst or "unknown time"
    local time_spent = submission.time_spent_minutes
    local time_label = "n/a"
    if time_spent ~= vim.NIL and time_spent ~= nil then
      time_label = tostring(time_spent) .. " min"
    end
    local result = submission.submit_result or "Unknown"
    local is_test = submission.is_test and "yes" or "no"

    table.insert(lines, string.format(
      "%d. submit=%s | time=%s | result=%s | test=%s",
      index,
      submitted_at,
      time_label,
      result,
      is_test
    ))
  end

  vim.notify(table.concat(lines, "\n"), vim.log.levels.INFO, {
    title = "Past submissions: " .. title_slug,
  })
end

function M.get_past_submissions(question, callback, limit)
  local title_slug = question.q.title_slug
  local response_line
  local function finish(response)
    debug_log("get_past_submissions finish response=" .. vim.inspect(response))
    if callback then
      callback(response)
      return
    end

    if response and response.error then
      vim.notify("⚠️  " .. response.error, vim.log.levels.ERROR)
      return
    end

    M.list_past_submissions(title_slug, (response and response.submissions) or {})
  end

  local request = json_request({
    action = "get_past_submissions",
    title_slug = title_slug,
    limit = limit or 10,
  })

  debug_log("get_past_submissions title_slug=" .. title_slug .. " limit=" .. tostring(limit or 10))

  send_request(request, {
    on_exit = function(_, exit_code, _)
      debug_log("on_exit exit_code=" .. tostring(exit_code) .. " response_line=" .. tostring(response_line))
      if exit_code ~= 0 then
        local msg = "Past submission lookup failed (code: " .. exit_code .. ")"
        vim.notify("⚠️  " .. msg, vim.log.levels.WARN)
        finish({ error = msg, submissions = {} })
        return
      end

      if not response_line then
        local msg = "Past submission lookup returned no data"
        vim.notify("⚠️  " .. msg, vim.log.levels.WARN)
        finish({ error = msg, submissions = {} })
        return
      end

      local ok, response = pcall(vim.fn.json_decode, response_line)
      if not ok then
        local msg = "Failed to parse past submissions response"
        vim.notify("⚠️  " .. msg, vim.log.levels.ERROR)
        debug_log("json_decode failed for line=" .. tostring(response_line))
        finish({ error = msg, submissions = {} })
        return
      end

      if response.error then
        vim.notify("⚠️  " .. response.error, vim.log.levels.ERROR)
        finish(response)
        return
      end

      finish(response)
    end,
    on_stdout = function(_, data, _)
      debug_log("on_stdout lines=" .. vim.inspect(data))
      response_line = extract_response_line(data) or response_line
      debug_log("response_line updated to " .. tostring(response_line))
    end,
    on_stderr = function(_, data, _)
      debug_log("on_stderr lines=" .. vim.inspect(data))
      if data and #data > 0 then
        for _, line in ipairs(data) do
          if line ~= "" and not line:match("^$") then
            vim.notify("Past submission error: " .. line, vim.log.levels.ERROR)
          end
        end
      end
    end,
  })
end

function M.show_past_submissions(question, limit)
  M.get_past_submissions(question, nil, limit)
end

local function format_mem0_recall_lines(response)
  local lines = {}
  local sessions = type(response.sessions) == "table" and response.sessions or {}
  local similar_matches = type(response.similar_matches) == "table" and response.similar_matches or {}

  table.insert(lines, string.format("之前做过这道题，找到了 %d 条历史记录。", tonumber(response.record_count) or #sessions))

  for index, session in ipairs(sessions) do
    local header = string.format("%d. %s", index, session.endReason or "unknown")
    if session.latestFailureStatus and session.latestFailureStatus ~= vim.NIL then
      header = header .. " | " .. session.latestFailureStatus
    end
    table.insert(lines, header)

    if session.failureSummary and session.failureSummary ~= vim.NIL and session.failureSummary ~= "" then
      table.insert(lines, "  之前的 failure: " .. session.failureSummary)
    end

    if type(session.stuckPoints) == "table" and #session.stuckPoints > 0 then
      table.insert(lines, "  当时卡点: " .. table.concat(session.stuckPoints, " | "))
    end

    if type(session.thoughtProcess) == "table" and #session.thoughtProcess > 0 then
      table.insert(lines, "  你的思路: " .. table.concat(session.thoughtProcess, " | "))
    end
  end

  if #similar_matches > 0 then
    table.insert(lines, "")
    table.insert(lines, string.format("还找到 %d 道类似题。", tonumber(response.similar_match_count) or #similar_matches))
    for index, match in ipairs(similar_matches) do
      local header = string.format("%d. %s", index, match.titleSlug or "unknown")
      if match.score and match.score ~= vim.NIL then
        header = header .. " | score=" .. tostring(match.score)
      end
      table.insert(lines, header)

      if match.profile and match.profile.problemSummary and match.profile.problemSummary ~= "" then
        table.insert(lines, "  为什么像: " .. match.profile.problemSummary)
      end

      if type(match.failureSummaries) == "table" and #match.failureSummaries > 0 then
        table.insert(lines, "  历史 failure: " .. table.concat(match.failureSummaries, " | "))
      end

      if type(match.stuckPoints) == "table" and #match.stuckPoints > 0 then
        table.insert(lines, "  当时卡点: " .. table.concat(match.stuckPoints, " | "))
      end
    end
  end

  return lines
end

function M.get_mem0_recall_summary(question, callback)
  local title_slug = question.q.title_slug
  local response_line

  local request = json_request({
    action = "get_mem0_recall_summary",
    title_slug = title_slug,
    title = question.q and question.q.title or "",
    difficulty = question.q and question.q.difficulty or "",
    question_content = question_description_text(question),
    topic_tags = question_topic_tags(question),
  })

  send_request(request, {
    timeout_ms = 10000,
    on_exit = function(_, exit_code, _)
      if exit_code ~= 0 then
        callback({
          success = false,
          error = "Mem0 recall lookup failed (code: " .. exit_code .. ")",
        })
        return
      end

      if not response_line then
        callback({
          success = false,
          error = "Mem0 recall lookup returned no data",
        })
        return
      end

      local ok, response = pcall(vim.fn.json_decode, response_line)
      if not ok then
        callback({
          success = false,
          error = "Failed to parse Mem0 recall response",
        })
        return
      end

      callback(response)
    end,
    on_stdout = function(_, data, _)
      response_line = extract_response_line(data) or response_line
    end,
  })
end

function M.show_mem0_recall_summary(question, opts)
  opts = opts or {}
  local title_slug = question.q.title_slug
  local now = vim.loop.hrtime() / 1000000
  local last_shown = shown_mem0_recall_at[title_slug] or 0

  if now - last_shown < (opts.debounce_ms or 3000) then
    return
  end

  shown_mem0_recall_at[title_slug] = now

  M.get_mem0_recall_summary(question, function(response)
    if not response or response.success == false then
      local message = response and response.error or "Mem0 recall lookup failed"
      debug_log("mem0 recall summary failed: " .. tostring(message))
      return
    end

    if not response.has_history and (tonumber(response.similar_match_count) or 0) == 0 then
      return
    end

    local lines = format_mem0_recall_lines(response)
    vim.notify(table.concat(lines, "\n"), vim.log.levels.INFO, {
      title = "LeetCode Memory: " .. title_slug,
      timeout = opts.timeout or 12000,
    })
  end)
end

function M.analyze_failure(question, buffer, item, callback)
  local title_slug = question.q.title_slug
  local content
  if type(buffer) == "table" then
    content = table.concat(buffer, "\n")
  else
    content = buffer or ""
  end

  local response_line
  local request = json_request({
    action = "analyze_failure",
    title_slug = title_slug,
    title = question.q and question.q.title or "",
    difficulty = question.q and question.q.difficulty or "",
    topic_tags = question_topic_tags(question),
    question_content = question_description_text(question),
    editor_content = content,
    submission_content = content,
    testcase = question.console and question.console.testcase and question.console.testcase:content() or "",
    filetype = analysis_filetype(question),
    item = item or {},
  })

  send_request(request, {
    timeout_ms = 30000,
    on_exit = function(_, exit_code, _)
      if exit_code ~= 0 then
        callback({
          success = false,
          error = "Failure analysis request failed (code: " .. exit_code .. ")",
          annotations = {},
        })
        return
      end

      if not response_line then
        callback({
          success = false,
          error = "Failure analysis returned no data",
          annotations = {},
        })
        return
      end

      local ok, response = pcall(vim.fn.json_decode, response_line)
      if not ok then
        callback({
          success = false,
          error = "Failed to parse failure analysis response",
          annotations = {},
        })
        return
      end

      if response and response.success and response.event_id then
        pcall(function()
          require("leetcode.integrations.codecompanion").render_failure_event(question, response)
        end)
      end

      if response and response.success then
        pcall(function()
          require("leetcode-ui.split.submissions").refresh_memory_for_slug(title_slug)
        end)
      end

      callback(response)
    end,
    on_stdout = function(_, data, _)
      response_line = extract_response_line(data) or response_line
    end,
    on_stderr = function(_, data, _)
      if data and #data > 0 then
        for _, line in ipairs(data) do
          if line ~= "" and not line:match("^$") then
            debug_log("Failure analysis error: " .. line)
          end
        end
      end
    end,
  })
end

return M
