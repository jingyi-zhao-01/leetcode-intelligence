# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: final-value-of-variable-after-performing-operations
# source_path: LeetCode-Solutions-master/Python/final-value-of-variable-after-performing-operations.py
# solution_class: Solution
# submission_id: b795bb243e6f74f4bfa9b026359d14142ecfe49c
# seed: 3457784483

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        return sum(1 if '+' == op[1] else -1 for op in operations)