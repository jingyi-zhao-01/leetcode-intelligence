---@diagnostic disable: undefined-global
-- Lua wrapper to save submissions to database
-- Replace the local filesystem write with database save via Python script

-- Usage in your LeetCode Neovim plugin config:
-- ["submit"] = {
--   function(question, buffer, status_msg, success)
--     require("submission_db_saver").save_submission(question, buffer, status_msg)
--   end,
-- }

local M = {}

-- Project root absolute path
local PROJECT_ROOT = "/home/jingyi/PycharmProjects/leetcode-qa"

function M.save_submission(question, buffer, item)
  -- Save submission to database using Python script.
  -- 
  -- Args:
  --   question: Question object with q.title_slug field
  --   buffer: Submission code content
  --   item: Full judge result item object containing status_msg and other fields
  
  -- Extract fields
  local title_slug = question.q.title_slug
  
  -- Extract status from item object
  local status_msg = item and item.status_msg or "unknown"
  local safe_status = status_msg:gsub("%s+", "_")
  
  -- Debug: Print the entire item object to see what's available
  -- vim.notify("Item object: " .. vim.inspect(item), vim.log.levels.DEBUG)
  


  -- Convert buffer to string (handle both array of lines and string)
  local content
  if type(buffer) == "table" then
    content = table.concat(buffer, "\n")
  else
    content = buffer or ""
  end

  -- Serialize the item object to JSON for passing to Python
  local item_json = vim.fn.json_encode(item or {})
  
  -- Write content and item to temporary files to avoid shell escaping issues
  local temp_dir = vim.fn.tempname()
  vim.fn.mkdir(temp_dir, "p")
  local content_file = temp_dir .. "/content.txt"
  local item_file = temp_dir .. "/item.json"
  
  vim.fn.writefile(vim.split(content, "\n"), content_file)
  vim.fn.writefile({item_json}, item_file)
  
  -- Build the command using file inputs
  local cmd = string.format(
    "cd '%s' && poetry run python -c 'import sys; import json; from src.submissions.submission_saver import save_submission; import asyncio; content = open(sys.argv[1]).read(); item = json.load(open(sys.argv[2])); asyncio.run(save_submission(sys.argv[3], content, item))' '%s' '%s' '%s'",
    PROJECT_ROOT,
    content_file,
    item_file,
    title_slug
  )
  
  -- Execute the command asynchronously
  vim.fn.jobstart(cmd, {
    on_exit = function(_, exit_code, _)
      -- Cleanup temp files
      vim.fn.delete(temp_dir, "rf")
      
      if exit_code == 0 then
        vim.notify("✓ Submission saved to database", vim.log.levels.INFO)
      else
        vim.notify("✗ Failed to save submission (exit code: " .. exit_code .. ")", vim.log.levels.ERROR)
      end
    end,
    on_stdout = function(_, data, _)
      if data and #data > 0 then
        for _, line in ipairs(data) do
          if line ~= "" then
            -- vim.notify(line, vim.log.levels.INFO)
          end
        end
      end
    end,
    on_stderr = function(_, data, _)
      if data and #data > 0 then
        for _, line in ipairs(data) do
          if line ~= "" then
            vim.notify("✗ " .. line, vim.log.levels.ERROR)
          end
        end
      end
    end,
  })
end

return M
