# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-deletions-to-make-array-divisible
# source_path: LeetCode-Solutions-master/Python/minimum-deletions-to-make-array-divisible.py
# solution_class: Solution
# submission_id: c4097f056e4d00f2779b3afe37e4b1488e34d38d
# seed: 1722731611

# Time:  O(n + m + logr), r is max(numsDivide)
# Space: O(1)

# gcd

class Solution(object):
    def minOperations(self, nums, numsDivide):
        """
        :type nums: List[int]
        :type numsDivide: List[int]
        :rtype: int
        """
        def gcd(a, b):  # Time: O(log(min(a, b)))
            while b:
                a, b = b, a%b
            return a

        g = reduce(gcd, numsDivide)
        mn = float("inf")
        for x in nums:
            if g%x == 0:
                mn = min(mn, x)
        return sum(x < mn for x in nums) if mn != float("inf") else -1