# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: construct-string-with-minimum-cost
# source_path: LeetCode-Solutions-master/Python/construct-string-with-minimum-cost.py
# solution_class: Solution
# submission_id: 8984e5aee3d4fa6f5e2e61c9543cc0068b5844db
# seed: 2664006831

# Time:  O(n^2 + w * l)
# Space: O(t)

import itertools


# trie, dp

class Solution(object):
    def minimumCost(self, target, words, costs):
        """
        :type target: str
        :type words: List[str]
        :type costs: List[int]
        :rtype: int
        """
        INF = float("inf")
        def query(i):
            curr = trie
            for j in xrange(i, len(target)):
                x = target[j]
                if x not in curr:
                    break
                curr = curr[x]
                if "_end" in curr:
                    dp[j+1] = min(dp[j+1], dp[i]+curr["_end"])

        _trie = lambda: collections.defaultdict(_trie)
        trie = _trie()
        for w, c in itertools.izip(words, costs):
            node = reduce(dict.__getitem__, w, trie)
            if "_end" not in node:
                node["_end"] = INF
            node["_end"] = min(node["_end"], c)
        dp = [INF]*(len(target)+1)
        dp[0] = 0
        for i in xrange(len(target)):
            if dp[i] == INF:
                continue
            query(i)
        return dp[-1] if dp[-1] != INF else -1