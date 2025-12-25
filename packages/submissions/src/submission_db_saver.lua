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

function M.start_timer(question)
  -- Start timer for a problem session via TCP server.
  --
  -- Args:
  --   question: Question object with q.title_slug field
  
  local title_slug = question.q.title_slug
  
  -- Send JSON request to server via TCP
  local request = vim.fn.json_encode({
    action = "start_timer",
    title_slug = title_slug
  }) .. "\n"
  
  -- Use printf and nc with explicit newline
  local cmd = string.format(
    "printf '%%s' '%s' | nc -N localhost 3000 2>&1",
    request:gsub("'", "'\\''")
  )
  
  vim.fn.jobstart(cmd, {
    on_exit = function(_, exit_code, _)
      if exit_code == 0 then
        vim.notify("⏱️  Started: " .. title_slug, vim.log.levels.INFO)
      else
        vim.notify("⚠️  Timer start failed (code: " .. exit_code .. ")", vim.log.levels.WARN)
      end
    end,
    on_stdout = function(_, data, _)
      if data and #data > 0 then
        for _, line in ipairs(data) do
          if line ~= "" then
            vim.notify("Timer response: " .. line, vim.log.levels.DEBUG)
          end
        end
      end
    end,
    on_stderr = function(_, data, _)
      if data and #data > 0 then
        for _, line in ipairs(data) do
          if line ~= "" and not line:match("^$") then
            vim.notify("Timer error: " .. line, vim.log.levels.ERROR)
          end
        end
      end
    end,
  })
end

return M
