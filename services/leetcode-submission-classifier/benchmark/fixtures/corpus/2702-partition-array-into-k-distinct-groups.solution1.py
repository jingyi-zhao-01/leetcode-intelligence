# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: partition-array-into-k-distinct-groups
# source_path: LeetCode-Solutions-master/Python/partition-array-into-k-distinct-groups.py
# solution_class: Solution
# submission_id: fc316afd507892b4941d3a799fa8733b673d8ff4
# seed: 555405239

# Time:  O(n)
# Space: O(n)

import collections


# math, freq table

class Solution(object):
    def partitionArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(nums)%k:
            return False
        group_cnt = len(nums)//k 
        cnt = collections.defaultdict(int)
        for x in nums:
            cnt[x] += 1 
        return all(x <= group_cnt for x in cnt.itervalues())