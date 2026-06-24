# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-distance-to-type-a-word-using-two-fingers
# source_path: LeetCode-Solutions-master/Python/minimum-distance-to-type-a-word-using-two-fingers.py
# solution_class: Solution2
# submission_id: cf9a6637cfe8cfbc914b83ac0bd3553347e32e43
# seed: 3419138149

# Time:  O(26n)
# Space: O(26)

class Solution2(object):
    def minimumDistance(self, word):
        """
        :type word: str
        :rtype: int
        """
        def distance(a, b):
            if -1 in [a, b]:
                return 0
            return abs(a//6 - b//6) + abs(a%6 - b%6)

        dp = {(-1, -1): 0}
        for c in word:
            c = ord(c)-ord('A')
            new_dp = {}
            for a, b in dp:
                new_dp[c, b] = min(new_dp.get((c, b), float("inf")), dp[a, b] + distance(a, c))
                new_dp[a, c] = min(new_dp.get((a, c), float("inf")), dp[a, b] + distance(b, c))
            dp = new_dp
        return min(dp.itervalues())