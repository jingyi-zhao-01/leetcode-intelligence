# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-ways-to-form-a-target-string-given-a-dictionary
# source_path: LeetCode-Solutions-master/Python/number-of-ways-to-form-a-target-string-given-a-dictionary.py
# solution_class: Solution
# submission_id: 2c8de6b274cdc55330c8daf927191e4a8a293a83
# seed: 3446204103

# Time:  O(l * (w + n)), l is the length of a word, w is the number of words, n is the length of target
# Space: O(n)

import collections


# optimized from Solution2

class Solution(object):
    def numWays(self, words, target):
        """
        :type words: List[str]
        :type target: str
        :rtype: int
        """
        MOD = 10**9+7
        dp = [0]*(len(target)+1)
        dp[0] = 1
        for i in xrange(len(words[0])):
            count = collections.Counter(w[i] for w in words)
            for j in reversed(xrange(len(target))):
                dp[j+1] += dp[j]*count[target[j]] % MOD
        return dp[-1] % MOD