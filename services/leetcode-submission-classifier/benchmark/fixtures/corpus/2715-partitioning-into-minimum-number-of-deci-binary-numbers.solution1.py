# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: partitioning-into-minimum-number-of-deci-binary-numbers
# source_path: LeetCode-Solutions-master/Python/partitioning-into-minimum-number-of-deci-binary-numbers.py
# solution_class: Solution
# submission_id: 7b1cc4507bbfeadd298cdc400aa0e82fc1e39b2c
# seed: 1275153358

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def minPartitions(self, n):
        """
        :type n: str
        :rtype: int
        """
        return int(max(n))