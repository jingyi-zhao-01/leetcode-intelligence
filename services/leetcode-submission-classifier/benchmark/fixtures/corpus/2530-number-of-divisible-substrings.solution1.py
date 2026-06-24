# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-divisible-substrings
# source_path: LeetCode-Solutions-master/Python/number-of-divisible-substrings.py
# solution_class: Solution
# submission_id: 72bc110929f1e3a0132d5548f0aa486cc6ccad97
# seed: 2911031374

# Time:  O(d * n)
# Space: O(n)

import collections


# prefix sum, freq table

class Solution(object):
    def countDivisibleSubstrings(self, word):
        """
        :type word: str
        :rtype: int
        """
        result = 0
        for d in xrange(1, 10):
            prefix = 0
            cnt = collections.Counter([0+d*(-1+1)])
            for i, x in enumerate(word):
                prefix += (ord(x)-ord('a')+1)//3+1
                result += cnt[prefix-d*(i+1)]
                cnt[prefix-d*(i+1)] += 1
        return result