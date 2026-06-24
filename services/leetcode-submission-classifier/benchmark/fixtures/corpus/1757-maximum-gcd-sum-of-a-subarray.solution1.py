# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-gcd-sum-of-a-subarray
# source_path: LeetCode-Solutions-master/Python/maximum-gcd-sum-of-a-subarray.py
# solution_class: Solution
# submission_id: d9a0d427666e81b1b5ea44dc64fc36b98433cc2e
# seed: 1382725192

# Time:  O(nlogr), r = max(nums)
# Space: O(logr)

# number theory, dp, prefix sum

class Solution(object):
    def maxGcdSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def gcd(a, b):
            while b:
                a, b = b, a%b
            return a

        result = prefix = 0
        dp = []
        for right, x in enumerate(nums):
            dp.append((right, x, prefix))
            prefix += x
            new_dp = []
            for left, g, p in dp:  # Time: O(logr)
                ng = gcd(g, x)  # Total Time: O(nlogr)
                if not new_dp or new_dp[-1][1] != ng:
                    new_dp.append((left, ng, p))  # left and ng are both strictly increasing
            dp = new_dp
            for left, g, p in dp:
                if right-left+1 < k:
                    break
                result = max(result, (prefix-p)*g)
        return result