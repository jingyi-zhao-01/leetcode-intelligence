# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: palindrome-removal
# source_path: LeetCode-Solutions-master/Python/palindrome-removal.py
# solution_class: Solution
# submission_id: 8028fab2a0934f73eb809243899947827e51142e
# seed: 3719112312

# Time:  O(n^3)
# Space: O(n^2)

class Solution(object):
    def minimumMoves(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        dp = [[0 for _ in xrange(len(arr)+1)] for _ in xrange(len(arr)+1)]
        for l in xrange(1, len(arr)+1):
            for i in xrange(len(arr)-l+1):
                j = i+l-1
                if l == 1:
                    dp[i][j] = 1
                else:
                    dp[i][j] = 1+dp[i+1][j]
                    if arr[i] == arr[i+1]:
                        dp[i][j] = min(dp[i][j], 1+dp[i+2][j])
                    for k in xrange(i+2, j+1):
                        if arr[i] == arr[k]:
                            dp[i][j] = min(dp[i][j], dp[i+1][k-1] + dp[k+1][j])
        return dp[0][len(arr)-1]