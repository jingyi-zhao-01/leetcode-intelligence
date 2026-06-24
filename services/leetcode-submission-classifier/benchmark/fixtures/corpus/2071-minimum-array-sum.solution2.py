# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-array-sum
# source_path: LeetCode-Solutions-master/Python/minimum-array-sum.py
# solution_class: Solution2
# submission_id: 07774176f475742a8f4a48084e736689df3ffd7a
# seed: 3500711656

# Time:  O(nlogn)
# Space: O(n)

# greedy, case works
# Reference: https://leetcode.com/problems/minimum-array-sum/solutions/6078002/o-n-log-n-greedy/

class Solution2(object):
    def minArraySum(self, nums, k, op1, op2):
        """
        :type nums: List[int]
        :type k: int
        :type op1: int
        :type op2: int
        :rtype: int
        """
        dp = [[sum(nums)]*(op2+1) for _ in xrange(op1+1)]
        for x in nums:
            for i in reversed(xrange(op1+1)):
                for j in reversed(xrange(op2+1)):
                    if i-1 >= 0:
                        dp[i][j] = min(dp[i][j], dp[i-1][j]-x+(x+1)//2)
                    if j-1 >= 0:
                        if x-k >= 0:
                            dp[i][j] = min(dp[i][j], dp[i][j-1]-x+(x-k))
                    if i-1 >= 0 and j-1 >= 0:
                        if x-k >= 0:
                            dp[i][j] = min(dp[i][j], dp[i-1][j-1]-x+((x-k)+1)//2)
                        if (x+1)//2-k >= 0:
                            dp[i][j] = min(dp[i][j], dp[i-1][j-1]-x+((x+1)//2-k))
        return dp[op1][op2]