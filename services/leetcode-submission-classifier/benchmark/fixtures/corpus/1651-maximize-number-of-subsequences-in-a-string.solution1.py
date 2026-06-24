# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximize-number-of-subsequences-in-a-string
# source_path: LeetCode-Solutions-master/Python/maximize-number-of-subsequences-in-a-string.py
# solution_class: Solution
# submission_id: 99f6a00a66728d43050af6ded49a6b5866809c8f
# seed: 2356372964

# Time:  O(n)
# Space: O(1)

# counting, greedy

class Solution(object):
    def maximumSubsequenceCount(self, text, pattern):
        """
        :type text: str
        :type pattern: str
        :rtype: int
        """
        result = cnt1 = cnt2 = 0
        for c in text:
            if c == pattern[1]:
                result += cnt1
                cnt2 += 1
            if c == pattern[0]:
                cnt1 += 1
        return result + max(cnt1, cnt2)  # add pattern[1] at back or pattern[0] at front