# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-seconds-to-equalize-a-circular-array
# source_path: LeetCode-Solutions-master/Python/minimum-seconds-to-equalize-a-circular-array.py
# solution_class: Solution
# submission_id: 609f14132bbb6334112d87c261c9820d67d2a950
# seed: 3733146167

# Time:  O(n)
# Space: O(n)

import collections


# hash table

class Solution(object):
    def minimumSeconds(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lookup = collections.defaultdict(int)
        dist = collections.defaultdict(int)
        for i in xrange(2*len(nums)):
            x = nums[i%len(nums)]
            dist[x] = max(dist[x], i-lookup[x])
            lookup[x] = i
        return min(dist.itervalues())//2