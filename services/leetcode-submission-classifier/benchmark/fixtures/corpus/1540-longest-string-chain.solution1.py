# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: longest-string-chain
# source_path: LeetCode-Solutions-master/Python/longest-string-chain.py
# solution_class: Solution
# submission_id: 5851007300be8248dc1fb37f3de5d8751ca5003c
# seed: 1599107291

# Time:  O(n * l^2)
# Space: O(n * l)

import collections

class Solution(object):
    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        words.sort(key=len)
        dp = collections.defaultdict(int)
        for w in words:
            for i in xrange(len(w)):
                dp[w] = max(dp[w], dp[w[:i]+w[i+1:]]+1)
        return max(dp.itervalues())