# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: sliding-subarray-beauty
# source_path: LeetCode-Solutions-master/Python/sliding-subarray-beauty.py
# solution_class: Solution
# submission_id: 5d868b99d41572281e3903c0adfb19682d1f3e1c
# seed: 4095477726

# Time:  O(nlogk)
# Space: O(k)

from sortedcontainers import SortedList


# sorted list, two pointers

class Solution(object):
    def getSubarrayBeauty(self, nums, k, x):
        """
        :type nums: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        result = []
        sl = SortedList()
        for i, v in enumerate(nums): 
            if i-k >= 0:
                sl.remove(nums[i-k])
            sl.add(v)
            if i-k+1 >= 0:
                result.append(min(sl[x-1], 0))
        return result 