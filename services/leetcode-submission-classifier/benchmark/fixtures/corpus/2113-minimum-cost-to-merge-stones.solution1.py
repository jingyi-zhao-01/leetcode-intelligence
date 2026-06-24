# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-cost-to-merge-stones
# source_path: LeetCode-Solutions-master/Python/minimum-cost-to-merge-stones.py
# solution_class: Solution
# submission_id: c8885596972c34ec88c0ddf8ea0a80d4ad6c18fc
# seed: 4051092298

# Time:  O(n^3 / k)
# Space: O(n^2)

class Solution(object):
    def mergeStones(self, stones, K):
        """
        :type stones: List[int]
        :type K: int
        :rtype: int
        """
        if (len(stones)-1) % (K-1):
            return -1
        prefix = [0]
        for x in stones:
            prefix.append(prefix[-1]+x)
        dp = [[0]*len(stones) for _ in xrange(len(stones))]
        for l in xrange(K-1, len(stones)):
            for i in xrange(len(stones)-l):
                dp[i][i+l] = min(dp[i][j]+dp[j+1][i+l] for j in xrange(i, i+l, K-1))
                if l % (K-1) == 0:
                    dp[i][i+l] += prefix[i+l+1] - prefix[i]
        return dp[0][len(stones)-1]