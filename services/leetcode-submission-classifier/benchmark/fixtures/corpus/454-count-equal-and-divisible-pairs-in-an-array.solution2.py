# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-equal-and-divisible-pairs-in-an-array
# source_path: LeetCode-Solutions-master/Python/count-equal-and-divisible-pairs-in-an-array.py
# solution_class: Solution2
# submission_id: 8f6ca32c37e480691ff6a586cf3062e920ab13ae
# seed: 2481887430

# Time:  O(nlogk + n * sqrt(k))
# Space: O(n + sqrt(k)), number of factors of k is at most sqrt(k)

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
    
        cnts = collections.defaultdict(collections.Counter)
        for i, x in enumerate(nums):
            cnts[x][gcd(i, k)] += 1
        result = 0
        for cnt in cnts.itervalues():
            for x in cnt.iterkeys():
                for y in cnt.iterkeys():
                    if x > y or x*y%k:
                        continue
                    result += cnt[x]*cnt[y] if x != y else cnt[x]*(cnt[x]-1)//2
        return result