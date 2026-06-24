# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: smallest-stable-index-i
# source_path: LeetCode-Solutions-master/Python/smallest-stable-index-i.py
# solution_class: Solution
# submission_id: 5345b80b57bd7b457dffdabf75ca216d9cc7163f
# seed: 2190031241

# Time:  O(n)
# Space: O(n)

# prefix sum

class Solution(object):
    def firstStableIndex(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        right = [float("inf")]*(len(nums)+1)
        for i in reversed(xrange(len(nums))):
            right[i] = min(right[i+1], nums[i])
        left = 0
        for i in xrange(len(nums)):
            left = max(left, nums[i])
            if left-right[i] <= k:
                return i
        return -1