# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-array-pairs-divisible-by-k
# source_path: LeetCode-Solutions-master/Python/count-array-pairs-divisible-by-k.py
# solution_class: Solution2
# submission_id: 6b486dc280f61a4d06dd3bfab648827e515a6ac2
# seed: 2333457815

# Time:  O(nlogk + sqrt(k)^2) = O(nlogk + k)
# Space: O(sqrt(k)), number of factors of k is at most sqrt(k)

import collections


# math, number theory

class Solution2(object):
    def countPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def gcd(x, y):
            while y:
                x, y = y, x%y
            return x

        result = 0
        gcds = collections.Counter()
        for x in nums:
            gcd_i = gcd(x, k)
            result += sum(cnt for gcd_j, cnt in gcds.iteritems() if gcd_i*gcd_j%k == 0)
            gcds[gcd_i] += 1
        return result