# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: longest-unequal-adjacent-groups-subsequence-ii
# source_path: LeetCode-Solutions-master/Python/longest-unequal-adjacent-groups-subsequence-ii.py
# solution_class: Solution3
# submission_id: bbc70ed0539970fd1dd9b58438eca63c37c004c8
# seed: 3344191753

# Time:  O(n^2)
# Space: O(n)

import itertools


# dp, backtracing

class Solution3(object):
    def getWordsInLongestSubsequence(self, n, words, groups):
        """
        :type n: int
        :type words: List[str]
        :type groups: List[int]
        :rtype: List[str]
        """
        def check(s1, s2):
            return len(s1) == len(s2) and sum(a != b for a, b in itertools.izip(s1, s2)) == 1

        dp = [[] for _ in xrange(n)]
        for i in xrange(n):
            for j in xrange(i):
                if groups[i] != groups[j] and check(words[j], words[i]) and len(dp[j]) > len(dp[i]):
                    dp[i] = dp[j]
            dp[i] = dp[i]+[i]
        return map(lambda x: words[x], max(dp, key=lambda x: len(x)))