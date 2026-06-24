# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: binary-search
# source_path: LeetCode-Solutions-master/Python/binary-search.py
# solution_class: Solution
# submission_id: 50a43fea82dbbf7b47898eb828765d436a138044
# seed: 3748785382

# Time:  O(logn)
# Space: O(1)

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums)-1
        while left <= right:
            mid = left + (right-left)//2
            if nums[mid] > target:
                right = mid-1
            elif nums[mid] < target:
                left = mid+1
            else:
                return mid
        return -1