# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-the-count-of-monotonic-pairs-i
# source_path: LeetCode-Solutions-master/Python/find-the-count-of-monotonic-pairs-i.py
# solution_class: Solution2
# submission_id: 82f3f248035027c5a52f2b804f0428324d41f494
# seed: 3624135965

# Time:  O(n + r), r = max(nums)
# Space: O(n + r)

# combinatorics, stars and bars

class Solution2(object):
    def countOfPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MOD = 10**9+7
        dp = [int(i <= nums[0]) for i in xrange(max(nums)+1)]  # dp[j]: numbers of arr1, which is of length i+1 and arr1[i] is j
        for i in xrange(1, len(nums)):
            # arr1[i-1] <= arr1[i]
            # => arr1[i]-arr1[i-1] >= 0 (1)
            #
            # arr2[i-1] >= arr2[i]
            # => nums[i-1]-arr1[i-1] >= nums[i]-arr1[i] 
            # => arr1[i]-arr1[i-1] >= nums[i]-nums[i-1] (2)
            #
            # (1)+(2): arr1[i]-arr1[i-1] >= max(nums[i]-nums[i-1], 0)
            new_dp = [0]*len(dp)
            diff = max(nums[i]-nums[i-1], 0)
            for j in xrange(diff, nums[i]+1):
                new_dp[j] = (new_dp[j-1]+dp[j-diff])%MOD
            dp = new_dp
        return reduce(lambda accu, x: (accu+x)%MOD, dp, 0)