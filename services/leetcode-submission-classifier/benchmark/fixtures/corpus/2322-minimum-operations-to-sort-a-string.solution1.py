# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-operations-to-sort-a-string
# source_path: LeetCode-Solutions-master/Python/minimum-operations-to-sort-a-string.py
# solution_class: Solution
# submission_id: c89bf2bb1b72b02c507e0517541dc8d90efe674c
# seed: 84642404

# Time:  O(n)
# Space: O(1)

# greedy

class Solution(object):
    def minOperations(self, s):
        """
        :type s: str
        :rtype: int
        """
        if all(s[i] <= s[i+1] for i in xrange(len(s)-1)):
            return 0
        if len(s) == 2:
            return -1
        mn = min(s[i] for i in xrange(1, len(s)-1))
        mx = max(s[i] for i in xrange(1, len(s)-1))
        return 1 if s[0] == min(s) or s[-1] == max(s) else 2 if s[-1] >= mn or s[0] <= mx else 3