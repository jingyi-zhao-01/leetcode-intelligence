# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-the-minimum-possible-sum-of-a-beautiful-array
# source_path: LeetCode-Solutions-master/Python/find-the-minimum-possible-sum-of-a-beautiful-array.py
# solution_class: Solution
# submission_id: 5539a5afb1e77be15a0d51d039b29aeb9b77282e
# seed: 2398368277

class Solution(object):
    def minimumPossibleSum(self, n, target):
        """
        :type n: int
        :type target: int
        :rtype: int
        """
        def arithmetic_progression_sum(a, d, n):
            return (a+(a+(n-1)*d))*n//2
    
        a = min(target//2, n)
        b = n-a
        return arithmetic_progression_sum(1, 1, a)+arithmetic_progression_sum(target, 1, b)