# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: armstrong-number
# source_path: LeetCode-Solutions-master/Python/armstrong-number.py
# solution_class: Solution
# submission_id: 7417e5fbe673a839fc924371c8f8029acc136ea1
# seed: 1961379677

# Time:  O(klogk)
# Space: O(k)

class Solution(object):
    def isArmstrong(self, N):
        """
        :type N: int
        :rtype: bool
        """
        n_str = str(N)
        return sum(int(i)**len(n_str) for i in n_str) == N