# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximize-subarray-gcd-score
# source_path: LeetCode-Solutions-master/Python/maximize-subarray-gcd-score.py
# solution_class: Solution2
# submission_id: 2eebc611ec40dbf9f2d60d228ff0ed3754f2fcb1
# seed: 1290225018

# Time:  O(nlogn * logr), r = max(nums)
# Space: O(n + logr)

# number theory, suffix-gcd states, dp, binary search

class Solution2(object):
    def maxGCDScore(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def gcd(a, b):
            while b:
                a, b = b, a%b
            return a

        def lower_bit(x):
            return x&-x

        result = 0
        for i in xrange(len(nums)):
            mn = float("inf")
            g = cnt = 0
            for j in xrange(i, len(nums)):
                g = gcd(g, nums[j])
                bit = lower_bit(nums[j])
                if bit < mn:
                    mn = bit
                    cnt = 0
                if bit == mn:
                    cnt += 1
                result = max(result, g*(j-i+1)*(2 if cnt <= k else 1))
                if g*(len(nums)-i)*2 <= result:
                    break
        return result