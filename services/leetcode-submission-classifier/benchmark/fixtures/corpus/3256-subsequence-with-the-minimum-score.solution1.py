# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: subsequence-with-the-minimum-score
# source_path: LeetCode-Solutions-master/Python/subsequence-with-the-minimum-score.py
# solution_class: Solution
# submission_id: b14096bb5830fd8be235f6dfcc93f014b0c971a1
# seed: 2484929889

# Time:  O(n)
# Space: O(n)

# two pointers, dp

class Solution(object):
    def minimumScore(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        right = [-1]*len(s)  # right[i]: min removed rightmost index in s[i:]
        j = len(t)-1
        for i in reversed(xrange(len(s))):
            if j >= 0 and t[j] == s[i]:
                j -= 1
            right[i] = j
        result = j+1
        left = 0  # left at i: max removed leftmost index in s[:i]
        for i in xrange(len(s)):
            result = max(min(result, right[i]-left+1), 0)
            if left < len(t) and t[left] == s[i]:
                left += 1
        result = min(result, len(t)-left)
        return result