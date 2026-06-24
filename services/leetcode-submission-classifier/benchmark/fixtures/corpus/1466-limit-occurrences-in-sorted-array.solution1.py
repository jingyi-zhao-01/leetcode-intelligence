# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: limit-occurrences-in-sorted-array
# source_path: LeetCode-Solutions-master/Python/limit-occurrences-in-sorted-array.py
# solution_class: Solution
# submission_id: 6628c2935d58107269fe1d239933c0a294a50bf0
# seed: 1642345342

# Time:  O(n)
# Space: O(1)

# array, inplace

class Solution(object):
    def limitOccurrences(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        i = 0
        for x in nums:
            if i-k >= 0 and nums[i-k] == x:
                continue
            nums[i] = x
            i += 1
        while len(nums) != i:
            nums.pop()
        return nums