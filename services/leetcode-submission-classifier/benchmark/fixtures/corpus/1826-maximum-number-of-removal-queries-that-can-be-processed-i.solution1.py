# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-number-of-removal-queries-that-can-be-processed-i
# source_path: LeetCode-Solutions-master/Python/maximum-number-of-removal-queries-that-can-be-processed-i.py
# solution_class: Solution
# submission_id: 60fb543b60e8532df296729306d477ef8d5c0f91
# seed: 1213185378

# Time:  O(n^2)
# Space: O(n^2)

# dp

class Solution(object):
    def maximumProcessableQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[int]
        :rtype: int
        """
        dp = [[float("-inf")]*len(nums) for _ in xrange(len(nums))]
        dp[0][-1] = 0
        for l in reversed(xrange(1, len(nums))):
            for i in xrange(len(nums)-(l-1)):
                j = i+(l-1)
                if i-1 >= 0:
                    dp[i][j] = max(dp[i][j], dp[i-1][j]+(1 if nums[i-1] >= queries[dp[i-1][j]] else 0))
                if j+1 < len(nums):
                    dp[i][j] = max(dp[i][j], dp[i][j+1]+(1 if nums[j+1] >= queries[dp[i][j+1]] else 0))
                if dp[i][j] == len(queries):
                    return len(queries)
        return max(dp[i][i]+(1 if nums[i] >= queries[dp[i][i]] else 0) for i in xrange(len(nums)))