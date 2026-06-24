# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: longest-binary-subsequence-less-than-or-equal-to-k
# source_path: LeetCode-Solutions-master/Python/longest-binary-subsequence-less-than-or-equal-to-k.py
# solution_class: Solution
# submission_id: a66a6255a512480bbad0746088aa514dcdd3b22b
# seed: 3675082333

# Time:  O(n)
# Space: O(1)

# greedy

class Solution(object):
    def longestSubsequence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        result, base = 0, 1
        for i in reversed(xrange(len(s))):
            if s[i] == '0':
                result += 1
            elif base <= k:
                k -= base
                result += 1
            if base <= k:
                base <<= 1
        return result