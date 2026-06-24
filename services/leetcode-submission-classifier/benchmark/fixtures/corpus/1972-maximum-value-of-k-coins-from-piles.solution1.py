# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-value-of-k-coins-from-piles
# source_path: LeetCode-Solutions-master/Python/maximum-value-of-k-coins-from-piles.py
# solution_class: Solution
# submission_id: 122ab4f778ffbd6a157a665f729844aeba9b3237
# seed: 4235861464

# Time:  O(min(n * k^2, m * k)), m = sum(len(pile) for pile in piles)
# Space: O(k)

# dp

class Solution(object):
    def maxValueOfCoins(self, piles, k):
        """
        :type piles: List[List[int]]
        :type k: int
        :rtype: int
        """
        dp = [0]
        for pile in piles:
            new_dp = [0]*min(len(dp)+len(pile), k+1)
            for i in xrange(len(dp)):
                curr = 0
                for j in xrange(min(k-i, len(pile))+1):
                    new_dp[i+j] = max(new_dp[i+j], dp[i]+curr)
                    curr += pile[j] if j < len(pile) else 0
            dp = new_dp
        return dp[-1]