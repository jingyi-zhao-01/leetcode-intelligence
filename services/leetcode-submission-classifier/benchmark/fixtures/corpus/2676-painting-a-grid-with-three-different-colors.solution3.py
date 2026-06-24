# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: painting-a-grid-with-three-different-colors
# source_path: LeetCode-Solutions-master/Python/painting-a-grid-with-three-different-colors.py
# solution_class: Solution3
# submission_id: c91555ed1b0183c46110e3069b7403e1245f4097
# seed: 3963404084

# Time:  O(m * 2^m + 3^m + 2^(3 * m) * logn) = O(2^(3 * m) * logn)
# Space: O(2^(2 * m))

import collections
import itertools


# better complexity for small m, super large n
# matrix exponentiation solution

class Solution3(object):
    def colorTheGrid(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        MOD = 10**9+7
        def normalize(basis, mask, lookup):  # compute and cache, at most O(3*2^(m-3)) time and space
            if mask not in lookup[basis]:
                norm = {}
                result, b = 0, basis
                while b:
                    x = mask//b%3
                    if x not in norm:
                        norm[x] = len(norm)
                    result += norm[x]*b
                    b //= 3
                lookup[basis][mask] = result
            return lookup[basis][mask]

        if m > n:
            m, n = n, m
        basis = b = 3**(m-1)
        lookup = collections.defaultdict(dict)
        dp = collections.Counter({0: 1})
        for idx in xrange(m*n):
            r, c = divmod(idx, m)
            # sliding window with size m doesn't cross rows:
            #   [3, 2, ..., 2] => 3*2^(m-1) combinations
            assert(r != 0 or c != 0 or len(dp) == 1)
            assert(r != 0 or c == 0 or len(dp) == 3*2**(c-1) // 3 // (2 if c >= 2 else 1))  # divided by 3 * 2 is since the first two colors are normalized to speed up performance
            assert(r == 0 or c != 0 or len(dp) == 3*2**(m-1) // 3 // (2 if m >= 2 else 1))  # divided by 3 * 2 is since the first two colors are normalized to speed up performance
            # sliding window with size m crosses rows:
            #   [*, ..., *, *, 3, 2, ..., 2] => 3*3 * 2^(m-2) combinations
            #   [2, ..., 2, 3, *, *, ..., *]
            assert(r == 0 or c == 0 or len(dp) == (1 if m == 1 else 2 if m == 2 else 3*3 * 2**(m-2) // 3 // 2))  # divided by 3 * 2 for m >= 3 is since the first two colors of window are normalized to speed up performance
            new_dp = collections.Counter()
            for mask, v in dp.iteritems():
                choices = {0, 1, 2}
                if r > 0:
                    choices.discard(mask%3)  # get up grid
                if c > 0:
                    choices.discard(mask//basis)  # get left grid
                for x in choices:
                    new_mask = normalize(basis//b, ((x*basis)+(mask//3))//b, lookup)*b  # encoding mask
                    new_dp[new_mask] = (new_dp[new_mask]+v)%MOD
            if b > 1:
                b //= 3
            dp = new_dp
        return reduce(lambda x,y: (x+y)%MOD, dp.itervalues(), 0)  # Time: O(2^m)