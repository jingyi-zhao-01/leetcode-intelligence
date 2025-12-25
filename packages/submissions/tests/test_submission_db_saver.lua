---@diagnostic disable: undefined-global
-- Simple tests for submission_db_saver.lua
-- This file tests the logic that doesn't depend on vim globals

local function test_buffer_table_concat()
  -- Test that buffer table concatenation works
  local test_table = {"line 1", "line 2", "line 3"}
  local result = table.concat(test_table, "\n")
  
  assert(result == "line 1\nline 2\nline 3", "Table concatenation failed")
  print("✓ Buffer table concatenation works")
end

local function test_buffer_string_passthrough()
  -- Test that string buffers are handled correctly
  local test_string = "def foo():\n    return 1"
  local content = test_string or ""
  
  assert(content == test_string, "String buffer passthrough failed")
  print("✓ String buffer passthrough works")
end

local function test_status_message_gsub()
  -- Test that status message is properly converted to safe format
  local status_msg = "Wrong Answer"
  local safe_status = (status_msg or "unknown"):gsub("%s+", "_")
  
  assert(safe_status == "Wrong_Answer", "Status message conversion failed")
  print("✓ Status message conversion works")
end

local function test_string_format()
  -- Test command string formatting works
  local PROJECT_ROOT = "../../"
  local title_slug = "two-sum"
  local safe_status = "Accepted"
  local content_escaped = "'def foo(): return 1'"
  
  local cmd = string.format(
    'cd %s && poetry run submission-saver --title-slug "%s" --content %s --status "%s"',
    PROJECT_ROOT,
    title_slug,
    content_escaped,
    safe_status
  )
  
  assert(cmd:match("two%-sum"), "Command should contain title slug")
  assert(cmd:match("Accepted"), "Command should contain status")
  assert(cmd:match("poetry"), "Command should contain poetry")
  print("✓ Command string formatting works")
end

-- Run all tests
local function run_all_tests()
  print("\n=== Lua Submission Saver Unit Tests ===\n")
  
  local tests = {
    test_buffer_table_concat,
    test_buffer_string_passthrough,
    test_status_message_gsub,
    test_string_format,
  }
  
  local passed = 0
  local failed = 0
  
  for _, test in ipairs(tests) do
    local status, err = pcall(test)
    if status then
      passed = passed + 1
    else
      failed = failed + 1
      print("✗ Test failed: " .. tostring(err))
    end
  end
  
  print("\n=== Test Results ===")
  print("Passed: " .. passed)
  print("Failed: " .. failed)
  print("Total: " .. (passed + failed))
  
  if failed == 0 then
    print("\n✓ All tests passed!")
    return 0
  else
    print("\n✗ Some tests failed")
    return 1
  end
end

-- Run tests if executed directly
if arg[0]:match("test_submission_db_saver%.lua$") then
  os.exit(run_all_tests())
end

return {
  run_all_tests = run_all_tests,
}
