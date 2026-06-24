# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-gcd-sum-of-a-subarray
# source_path: LeetCode-Solutions-master/Python/maximum-gcd-sum-of-a-subarray.py
# solution_class: Solution2
# submission_id: 5236264004bc24bb14e4afc1e4f4d812ab56cdef
# seed: 4071628637

# Time:  O(nlogr), r = max(nums)
# Space: O(logr)

# number theory, dp, prefix sum

class Solution2(object):
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

        prefix = [0]*(len(nums)+1)
        for i, x in enumerate(nums):
            prefix[i+1] = prefix[i]+x
        result = 0
        dp = []
        for right, x in enumerate(nums):
            dp.append((right, x))
            new_dp = []
            for left, g in dp:  # Time: O(logr)
                ng = gcd(g, x)  # Total Time: O(nlogr)
                if not new_dp or new_dp[-1][1] != ng:
                    new_dp.append((left, ng))  # left and ng are both strictly increasing
            dp = new_dp
            for left, g in dp:
                if right-left+1 < k:
                    break
                result = max(result, (prefix[right+1]-prefix[left])*g)
        return result