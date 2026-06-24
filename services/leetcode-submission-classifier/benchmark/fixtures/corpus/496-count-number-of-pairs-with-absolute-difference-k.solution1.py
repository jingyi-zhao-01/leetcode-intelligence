# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-number-of-pairs-with-absolute-difference-k
# source_path: LeetCode-Solutions-master/Python/count-number-of-pairs-with-absolute-difference-k.py
# solution_class: Solution
# submission_id: 6e67403973d9588036030ae0a03379192a0eec73
# seed: 237710732

# Time:  O(n)
# Space: O(n)

import collections

class Solution(object):
    def countKDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        lookup = collections.defaultdict(int)
        result = 0
        for x in nums:
            if x-k in lookup:
                result += lookup[x-k]
            if x+k in lookup:
                result += lookup[x+k]
            lookup[x] += 1            
        return result