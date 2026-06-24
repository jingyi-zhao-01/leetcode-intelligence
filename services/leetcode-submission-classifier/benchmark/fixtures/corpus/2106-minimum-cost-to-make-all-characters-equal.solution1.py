# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-cost-to-make-all-characters-equal
# source_path: LeetCode-Solutions-master/Python/minimum-cost-to-make-all-characters-equal.py
# solution_class: Solution
# submission_id: b00d3a048168e0ac2c8c3ec512d3dcfa6d8e66ce
# seed: 1605180751

# Time:  O(n)
# Space: O(1)

# greedy

class Solution(object):
    def minimumCost(self, s):
        """
        :type s: str
        :rtype: int
        """
        return sum(min(i+1, len(s)-(i+1)) for i in xrange(len(s)-1) if s[i] != s[i+1])