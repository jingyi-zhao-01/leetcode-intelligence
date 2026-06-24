# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-the-maximum-sequence-value-of-array
# source_path: LeetCode-Solutions-master/Python/find-the-maximum-sequence-value-of-array.py
# solution_class: Solution
# submission_id: 87672b32fcd85cb42aedfebc50eaddc5a27e1b67
# seed: 4154619229

# Time:  O(n * r + r^2)
# Space: O(r)

# bitmasks, prefix sum, dp

class Solution(object):
    def maxValue(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        INF = float("inf")
        MAX_MASK = 127
        def is_submask(a, b):
            return (a|b) == b

        def dp(direction, npos):
            result = [npos]*(MAX_MASK+1)
            dp = [INF]*(MAX_MASK+1)
            cnt = [0]*(MAX_MASK+1)
            for i in direction(xrange(len(nums))):
                dp[nums[i]] = 1
                for mask in xrange(MAX_MASK+1):
                    if is_submask(nums[i], mask):
                        cnt[mask] += 1
                    dp[mask|nums[i]] = min(dp[mask|nums[i]], dp[mask]+1)
                for mask in xrange(MAX_MASK+1):
                    if cnt[mask] >= k and dp[mask] <= k and result[mask] == npos:
                        result[mask] = i
            return result

        left = dp(lambda x: x, len(nums))
        right = dp(reversed, -1)
        return next(result for result in reversed(xrange(MAX_MASK+1)) for l in xrange(1, MAX_MASK+1) if left[l] < right[result^l])