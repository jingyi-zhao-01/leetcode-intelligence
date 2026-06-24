# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-array-pairs-divisible-by-k
# source_path: LeetCode-Solutions-master/Python/count-array-pairs-divisible-by-k.py
# solution_class: Solution
# submission_id: cbe17e8e9261b562b664210bceb4b047c9177d7e
# seed: 3338712258

# Time:  O(nlogk + sqrt(k)^2) = O(nlogk + k)
# Space: O(sqrt(k)), number of factors of k is at most sqrt(k)

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
    
        cnt = collections.Counter()
        for x in nums:
            cnt[gcd(x, k)] += 1
        result = 0
        for x in cnt.iterkeys():
            for y in cnt.iterkeys():
                if x > y or x*y%k:
                    continue
                result += cnt[x]*cnt[y] if x != y else cnt[x]*(cnt[x]-1)//2
        return result