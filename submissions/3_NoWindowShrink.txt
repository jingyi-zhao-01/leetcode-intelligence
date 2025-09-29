# Problem 3. Longest Substring Without Repeating Characters
# Error: did not shrink window on duplicate -> quadratic scan

def lengthOfLongestSubstring(s):
    seen = {}
    left = 0
    best = 0
    for right, ch in enumerate(s):
        if ch in seen:
            # BUG: not moving left correctly; should move left = max(left, seen[ch] + 1)
            pass
        seen[ch] = right
        best = max(best, right - left + 1)
    return best
