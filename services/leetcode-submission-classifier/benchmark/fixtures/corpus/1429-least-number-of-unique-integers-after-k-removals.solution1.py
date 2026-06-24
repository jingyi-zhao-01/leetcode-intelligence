# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: least-number-of-unique-integers-after-k-removals
# source_path: LeetCode-Solutions-master/Python/least-number-of-unique-integers-after-k-removals.py
# solution_class: Solution
# submission_id: 88567485e9cf168e3c250874802e80121a24515a
# seed: 4272805416

# Time:  O(n)
# Space: O(n)

import collections

class Solution(object):
    def findLeastNumOfUniqueInts(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        count = collections.Counter(arr)
        result, count_count = len(count), collections.Counter(count.itervalues())
        for c in xrange(1, len(arr)+1): 
            if k < c*count_count[c]:
                result -= k//c
                break
            k -= c*count_count[c]
            result -= count_count[c]                
        return result