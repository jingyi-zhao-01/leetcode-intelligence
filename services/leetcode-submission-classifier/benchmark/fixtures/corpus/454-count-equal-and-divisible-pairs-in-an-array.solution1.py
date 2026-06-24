# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-equal-and-divisible-pairs-in-an-array
# source_path: LeetCode-Solutions-master/Python/count-equal-and-divisible-pairs-in-an-array.py
# solution_class: Solution
# submission_id: f55dfba2aa360355fa620299175764f6c07343be
# seed: 335741027

# Time:  O(nlogk + n * sqrt(k))
# Space: O(n + sqrt(k)), number of factors of k is at most sqrt(k)

import collections


# math, number theory

class Solution(object):
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
    
        idxs = collections.defaultdict(list)
        for i, x in enumerate(nums):
            idxs[x].append(i)
        result = 0
        for idx in idxs.itervalues():
            gcds = collections.Counter()
            for i in idx:
                gcd_i = gcd(i, k)
                result += sum(cnt for gcd_j, cnt in gcds.iteritems() if gcd_i*gcd_j%k == 0)
                gcds[gcd_i] += 1
        return result