# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: construct-string-with-minimum-cost-easy
# source_path: LeetCode-Solutions-master/Python/construct-string-with-minimum-cost-easy.py
# solution_class: Solution
# submission_id: 3d7bdd2ac33c214771cb9efe86f88a381c854eda
# seed: 1713154024

# Time:  O(n * w * l)
# Space: O(l)

import itertools


# dp

class Solution(object):
    def minimumCost(self, target, words, costs):
        """
        :type target: str
        :type words: List[str]
        :type costs: List[int]
        :rtype: int
        """
        INF = float("inf")
        l = max(len(w) for w in words)
        dp = [INF]*(l+1)
        dp[0] = 0
        for i in xrange(len(target)):
            if dp[i%len(dp)] == INF:
                continue
            for w, c in itertools.izip(words, costs):
                if target[i:i+len(w)] == w:
                    dp[(i+len(w))%len(dp)] = min(dp[(i+len(w))%len(dp)], dp[i%len(dp)]+c)
            dp[i%len(dp)] = INF
        return dp[len(target)%len(dp)] if dp[len(target)%len(dp)] != INF else -1