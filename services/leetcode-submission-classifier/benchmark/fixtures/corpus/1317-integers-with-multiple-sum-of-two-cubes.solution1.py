# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: integers-with-multiple-sum-of-two-cubes
# source_path: LeetCode-Solutions-master/Python/integers-with-multiple-sum-of-two-cubes.py
# solution_class: Solution
# submission_id: 17db2874dd81e21d5db1ab9f021b17f14c570bfa
# seed: 1222200423

# Time:  O(n^(2/3) * logn)
# Space: O(n^(2/3))

import collections


# brute force, freq table, sort

class Solution(object):
    def findGoodIntegers(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        cnt = collections.defaultdict(int)
        for i in xrange(1, n+1):
            if i**3 > n:
                break
            for j in xrange(i, (n-i**3)+1):
                if j**3 > n-i**3:
                    break
                cnt[i**3+j**3] += 1
        return sorted(k for k, v in cnt.iteritems() if v >= 2)