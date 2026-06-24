# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-ways-to-reorder-array-to-get-same-bst
# source_path: LeetCode-Solutions-master/Python/number-of-ways-to-reorder-array-to-get-same-bst.py
# solution_class: Solution
# submission_id: 119bcd9056d8e3e1339d7053c377fbf3ad809341
# seed: 937367490

# Time:  O(n^2)
# Space: O(n^2)

MAX_N = 1000
MOD = 10**9+7
dp = [[0]*MAX_N for _ in xrange(MAX_N)]
for i in xrange(len(dp)):
    dp[i][0] = 1
    for j in xrange(1, i+1):
        dp[i][j] = (dp[i-1][j-1] + dp[i-1][j])%MOD

class Solution(object):
    def numOfWays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def dfs(nums):
            if len(nums) <= 2:
                return 1
            left = [v for v in nums if v < nums[0]]
            right = [v for v in nums if v > nums[0]]
            result = dp[len(left)+len(right)][len(left)]
            result = result*dfs(left) % MOD
            result = result*dfs(right) % MOD
            return result

        return (dfs(nums)-1)%MOD