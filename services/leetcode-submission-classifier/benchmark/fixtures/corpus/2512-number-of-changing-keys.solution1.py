# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-changing-keys
# source_path: LeetCode-Solutions-master/Python/number-of-changing-keys.py
# solution_class: Solution
# submission_id: 7c4e26fdfa38f331d385d8be71ca85d89c39a209
# seed: 2573078763

# Time:  O(n)
# Space: O(1)

# string

class Solution(object):
    def countKeyChanges(self, s):
        """
        :type s: str
        :rtype: int
        """
        return sum(s[i].lower() != s[i+1].lower() for i in xrange(len(s)-1))