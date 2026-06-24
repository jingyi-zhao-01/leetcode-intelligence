# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-good-meals
# source_path: LeetCode-Solutions-master/Python/count-good-meals.py
# solution_class: Solution
# submission_id: b1930d6cfc3de1e7332ae39a64ad5c61dc449200
# seed: 639627394

# Time:  O(n)
# Space: O(1)

import collections

class Solution(object):
    def countPairs(self, deliciousness):
        """
        :type deliciousness: List[int]
        :rtype: int
        """
        def floor_log2_x(x):
            return x.bit_length()-1

        MOD = 10**9+7
        max_pow = floor_log2_x(max(deliciousness))+1
        cnt = collections.Counter()
        result = 0
        for d in deliciousness:
            p = 1
            for i in xrange(max_pow+1):
                result = (result+cnt[p-d])%MOD
                p <<= 1
            cnt[d] += 1    
        return result