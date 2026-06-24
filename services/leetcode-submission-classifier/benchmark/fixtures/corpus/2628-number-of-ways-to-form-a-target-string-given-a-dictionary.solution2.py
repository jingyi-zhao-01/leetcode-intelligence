# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-ways-to-form-a-target-string-given-a-dictionary
# source_path: LeetCode-Solutions-master/Python/number-of-ways-to-form-a-target-string-given-a-dictionary.py
# solution_class: Solution2
# submission_id: f9303788ac15496f6ebfc796aef5c285cfc3a59a
# seed: 1813743064

# Time:  O(l * (w + n)), l is the length of a word, w is the number of words, n is the length of target
# Space: O(n)

import collections


# optimized from Solution2

class Solution2(object):
    def numWays(self, words, target):
        """
        :type words: List[str]
        :type target: str
        :rtype: int
        """
        MOD = 10**9+7
        # dp[i+1][j+1]: number of ways of target[0..j] using count[0..i].
        dp = [[0]*(len(target)+1) for _ in xrange(2)]
        for i in xrange(len(dp)):
            dp[i][0] = 1
        for i in xrange(len(words[0])):
            count = collections.Counter(w[i] for w in words)
            for j in reversed(xrange(len(target))):
                dp[(i+1)%2][j+1] = dp[i%2][j+1]+dp[i%2][j]*count[target[j]] % MOD
        return dp[(len(words[0]))%2][-1] % MOD