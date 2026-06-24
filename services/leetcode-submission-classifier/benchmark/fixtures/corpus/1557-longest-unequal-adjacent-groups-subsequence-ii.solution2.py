# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: longest-unequal-adjacent-groups-subsequence-ii
# source_path: LeetCode-Solutions-master/Python/longest-unequal-adjacent-groups-subsequence-ii.py
# solution_class: Solution2
# submission_id: 294824f2503c5a7a4082de7da14c7dbe08999ac9
# seed: 1873119983

# Time:  O(n^2)
# Space: O(n)

import itertools


# dp, backtracing

class Solution2(object):
    def getWordsInLongestSubsequence(self, n, words, groups):
        """
        :type n: int
        :type words: List[str]
        :type groups: List[int]
        :rtype: List[str]
        """
        def check(s1, s2):
            return len(s1) == len(s2) and sum(a != b for a, b in itertools.izip(s1, s2)) == 1

        dp = [[1, -1] for _ in xrange(n)]
        for i in xrange(n):
            for j in xrange(i):
                if groups[i] != groups[j] and check(words[j], words[i]):
                    dp[i] = max(dp[i], [dp[j][0]+1, j])
        result = []
        i = max(xrange(n), key=lambda x: dp[x])
        while i != -1:
            result.append(words[i])
            i = dp[i][1]
        result.reverse()
        return result