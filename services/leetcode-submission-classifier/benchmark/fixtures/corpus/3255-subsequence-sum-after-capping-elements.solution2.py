# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: subsequence-sum-after-capping-elements
# source_path: LeetCode-Solutions-master/Python/subsequence-sum-after-capping-elements.py
# solution_class: Solution2
# submission_id: ccdddf0d7d6b0177d1ba4a60695a7ba68f554659
# seed: 815891221

# Time:  O(nlogn + n * k + klogn) = O(nlogn + n * k)
# Space: O(k)

# sort, dp, bitmasks

class Solution2(object):
    def subsequenceSumAfterCapping(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[bool]
        """
        result = [False]*len(nums)
        nums.sort()
        dp = [False]*(k+1)
        dp[0] = True
        i = 0
        for x in xrange(1, len(nums)+1):
            while i < len(nums) and nums[i] < x:
                for j in reversed(xrange(nums[i], k+1)):
                    dp[j] = dp[j] or dp[j-nums[i]]
                i += 1
            for j in xrange(max(k%x, k-(len(nums)-i)*x), k+1, x):
                if dp[j]:
                    result[x-1] = True
                    break
        return result