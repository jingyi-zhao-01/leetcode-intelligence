# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: library-late-fee-calculator
# source_path: LeetCode-Solutions-master/Python/library-late-fee-calculator.py
# solution_class: Solution
# submission_id: bcb2a6e181b22af065222eaa804470a81557a371
# seed: 2413688143

# Time:  O(n)
# Space: O(1)

# array

class Solution(object):
    def lateFee(self, daysLate):
        """
        :type daysLate: List[int]
        :rtype: int
        """
        return sum(1 if i == 1 else 3*i if i >= 6 else 2*i for i in daysLate)