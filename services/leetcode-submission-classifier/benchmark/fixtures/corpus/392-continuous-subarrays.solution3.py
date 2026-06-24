# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: continuous-subarrays
# source_path: LeetCode-Solutions-master/Python/continuous-subarrays.py
# solution_class: Solution3
# submission_id: d3f3338e496c7651bd15bcb5c1b7c12edf1200e4
# seed: 1126892731

# Time:  O(n)
# Space: O(1)

import collections


# two pointers

class Solution3(object):
    def continuousSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = left = 0
        lookup = SortedDict()
        for right in xrange(len(nums)):
            lookup[nums[right]] = right
            to_del = []
            for x, i in lookup.items():
                if nums[right]-x <= 2:
                    break
                left = max(left, i+1)
                to_del.append(x)
            for x, i in reversed(lookup.items()):
                if x-nums[right] <= 2:
                    break
                left = max(left, i+1)
                to_del.append(x) 
            for x in to_del:
                del lookup[x]
            result += right-left+1
        return result