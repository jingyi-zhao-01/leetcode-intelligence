# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: shortest-unsorted-continuous-subarray
# source_path: LeetCode-Solutions-master/Python/shortest-unsorted-continuous-subarray.py
# solution_class: Solution2
# submission_id: 520129b0a3903a172a7dcf2d3a228bbdcbf731cd
# seed: 595099138

# Time:  O(n)
# Space: O(1)

class Solution2(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = sorted(nums) #sort the list
        left, right = 0, len(nums) -1 #define left and right pointer
        while (nums[left] == a[left] or nums[right] == a[right]):
            if right - left <= 1:
                return 0
            if nums[left] == a[left]:
                left += 1
            if nums[right] == a[right]:
                right -= 1
        return right - left + 1