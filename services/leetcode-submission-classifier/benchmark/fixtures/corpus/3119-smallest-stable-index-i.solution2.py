# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: smallest-stable-index-i
# source_path: LeetCode-Solutions-master/Python/smallest-stable-index-i.py
# solution_class: Solution2
# submission_id: 10e3d5841bb82f220e7f6591288a9f4ae2e1212a
# seed: 3247802919

# Time:  O(n)
# Space: O(n)

# prefix sum

class Solution2(object):
    def firstStableIndex(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left = [0]*(len(nums)+1)
        for i in xrange(len(nums)):
            left[i+1] = max(left[i], nums[i])
        right = [float("inf")]*(len(nums)+1)
        for i in reversed(xrange(len(nums))):
            right[i] = min(right[i+1], nums[i])
        return next((i for i in xrange(len(nums)) if left[i+1]-right[i] <= k), -1)