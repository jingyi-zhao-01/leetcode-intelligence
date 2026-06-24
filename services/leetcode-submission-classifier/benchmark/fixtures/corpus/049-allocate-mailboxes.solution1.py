# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: allocate-mailboxes
# source_path: LeetCode-Solutions-master/Python/allocate-mailboxes.py
# solution_class: Solution
# submission_id: 1f03ac1657c8bbd151c8cb137dbbe4bcac9eff8a
# seed: 365403980

# Time:  O(m * n^2)
# Space: O(n)

class Solution(object):
    def minDistance(self, houses, k):
        """
        :type houses: List[int]
        :type k: int
        :rtype: int
        """
        def cost(prefix, i, j):
            return (prefix[j+1]-prefix[(i+j+1)//2])-(prefix[(i+j)//2+1]-prefix[i])

        houses.sort()
        prefix = [0]*(len(houses)+1)
        for i, h in enumerate(houses):
            prefix[i+1] = prefix[i]+h
        dp = [cost(prefix, 0, j) for j in xrange(len(houses))]
        for m in xrange(1, k):
            for j in reversed(xrange(m, len(houses))):
                for i in xrange(m, j+1):
                    dp[j] = min(dp[j], dp[i-1]+cost(prefix, i, j))
        return dp[-1]