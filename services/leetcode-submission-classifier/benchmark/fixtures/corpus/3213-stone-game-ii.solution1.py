# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: stone-game-ii
# source_path: LeetCode-Solutions-master/Python/stone-game-ii.py
# solution_class: Solution
# submission_id: 2bebc840b709ece311cdeca10eba4678b411ab0b
# seed: 207093609

# Time:  O(n*(logn)^2)
# Space: O(nlogn)

class Solution(object):
    def stoneGameII(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        def dp(piles, lookup, i, m):
            if i+2*m >= len(piles):
                return piles[i]
            if (i, m) not in lookup:
                lookup[i, m] = piles[i] - \
                               min(dp(piles, lookup, i+x, max(m, x))
                                   for x in xrange(1, 2*m+1))
            return lookup[i, m]

        for i in reversed(xrange(len(piles)-1)):
            piles[i] += piles[i+1]
        return dp(piles, {}, 0, 1)