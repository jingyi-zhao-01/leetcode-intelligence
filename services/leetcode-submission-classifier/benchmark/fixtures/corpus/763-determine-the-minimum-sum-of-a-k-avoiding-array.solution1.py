# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: determine-the-minimum-sum-of-a-k-avoiding-array
# source_path: LeetCode-Solutions-master/Python/determine-the-minimum-sum-of-a-k-avoiding-array.py
# solution_class: Solution
# submission_id: 112bfe67de5da469b4fada3d8bdb9420570b243d
# seed: 1843000979

# Time:  O(1)
# Space: O(1)

# constructive algorithms, math

class Solution(object):
    def minimumSum(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        def arithmetic_progression_sum(a, d, n):
            return (a+(a+(n-1)*d))*n//2
    
        a = min(k//2, n)
        b = n-a
        return arithmetic_progression_sum(1, 1, a)+arithmetic_progression_sum(k, 1, b)