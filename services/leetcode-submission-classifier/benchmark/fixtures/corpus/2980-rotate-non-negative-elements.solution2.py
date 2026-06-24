# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: rotate-non-negative-elements
# source_path: LeetCode-Solutions-master/Python/rotate-non-negative-elements.py
# solution_class: Solution2
# submission_id: 10159885c0d067da2e34a8ff502158610e24a70d
# seed: 1316692428

# Time:  O(n)
# Space: O(n)

# array

class Solution2(object):
    def rotateElements(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        def reverse(nums, left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
    
        def rotate(nums, k):
            k %= len(nums)
            reverse(nums, 0, len(nums)-1)
            reverse(nums, 0, len(nums)-k-1)
            reverse(nums, len(nums)-k, len(nums)-1)

        result = [x for x in nums if x >= 0]
        if not result:
            return nums
        rotate(result, k)
        j = 0
        for i in xrange(len(nums)):
            if nums[i] < 0:
                continue
            nums[i] = result[j]
            j += 1
        return nums