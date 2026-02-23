---@diagnostic disable: undefined-global
-- Lua wrapper to save submissions to database
-- Uses TCP connection to submission_server.py for both timer and submission operations


local M = {}

function M.save_submission(question, buffer, item)
  -- Save submission to database via TCP server.
  -- 
  -- Args:
  --   question: Question object with q.title_slug field
  --   buffer: Submission code content
  --   item: Full judge result item object containing status_msg and other fields
  
  local title_slug = question.q.title_slug
  
  -- Convert buffer to string (handle both array of lines and string)
  local content
  if type(buffer) == "table" then
    content = table.concat(buffer, "\n")
  else
    content = buffer or ""
  end

  -- Build JSON request
  local request = vim.fn.json_encode({
    action = "save_submission",
    title_slug = title_slug,
    content = content,
    item = item or {}
  }) .. "\n"
  
  -- Send JSON request to server via TCP
  local cmd = string.format(
    "printf '%%s' '%s' | nc -N localhost 3000 2>&1",
    request:gsub("'", "'\\''")
  )
  
  vim.fn.jobstart(cmd, {
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

  local request = vim.fn.json_encode({
    action = "start_timer",
    title_slug = title_slug
    -- allow_multiple defaults to False on the server side,
    -- so all existing timers are cleared and a fresh one is started.
  }) .. "\n"

  local cmd = string.format(
    "printf '%%s' '%s' | nc -N localhost 3000 2>&1",
    request:gsub("'", "'\\''")
  )

  vim.fn.jobstart(cmd, {
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

  local request = vim.fn.json_encode({
    action = "drop_timer",
    title_slug = title_slug,
  }) .. "\n"

  local cmd = string.format(
    "printf '%%s' '%s' | nc -N localhost 3000 2>&1",
    request:gsub("'", "'\\''")
  )

  vim.fn.jobstart(cmd, {
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

return M
