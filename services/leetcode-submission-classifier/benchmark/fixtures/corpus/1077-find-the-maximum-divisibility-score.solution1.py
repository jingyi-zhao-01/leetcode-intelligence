# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-the-maximum-divisibility-score
# source_path: LeetCode-Solutions-master/Python/find-the-maximum-divisibility-score.py
# solution_class: Solution
# submission_id: 580a6a18484b18072b3255133562a39c12934933
# seed: 3380693632

# Time:  O(n * d)
# Space: O(1)

# brute force

class Solution(object):
    def maxDivScore(self, nums, divisors):
        """
        :type nums: List[int]
        :type divisors: List[int]
        :rtype: int
        """
        return max(divisors, key=lambda d: (sum(x%d == 0 for x in nums), -d))