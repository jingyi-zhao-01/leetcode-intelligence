# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: stone-game-v
# source_path: LeetCode-Solutions-master/Python/stone-game-v.py
# solution_class: Solution
# submission_id: 835e11784729278f43f9a724260c64cfae6cfa5a
# seed: 3311011711

# Time:  O(n^2)
# Space: O(n^2)

class Solution(object):
    def stoneGameV(self, stoneValue):
        """
        :type stoneValue: List[int]
        :rtype: int
        """
        n = len(stoneValue)
        prefix = [0]
        for v in stoneValue:
            prefix.append(prefix[-1] + v)

        mid = range(n)

        dp = [[0]*n for _ in xrange(n)]
        for i in xrange(n):
            dp[i][i] = stoneValue[i]

        max_score = 0
        for l in xrange(2, n+1):
            for i in xrange(n-l+1):
                j = i+l-1
                while prefix[mid[i]]-prefix[i] < prefix[j+1]-prefix[mid[i]]:
                    mid[i] += 1  # Time: O(n^2) in total
                p = mid[i]
                max_score = 0
                if prefix[p]-prefix[i] == prefix[j+1]-prefix[p]:
                    max_score = max(dp[i][p-1], dp[j][p])
                else:
                    if i <= p-2:
                        max_score = max(max_score, dp[i][p-2])
                    if p <= j:
                        max_score = max(max_score, dp[j][p])
                dp[i][j] = max(dp[i][j-1], (prefix[j+1]-prefix[i]) + max_score)
                dp[j][i] = max(dp[j][i+1], (prefix[j+1]-prefix[i]) + max_score)
        return max_score