# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: apply-bitwise-operations-to-make-strings-equal
# source_path: LeetCode-Solutions-master/Python/apply-bitwise-operations-to-make-strings-equal.py
# solution_class: Solution
# submission_id: 98142691858363cab5eefb7d208f6ebeb70d89ad
# seed: 2962214243

# Time:  O(n)
# Space: O(1)

# constructive algorithms

class Solution(object):
    def makeStringsEqual(self, s, target):
        """
        :type s: str
        :type target: str
        :rtype: bool
        """
        return ('1' in s) == ('1' in target)