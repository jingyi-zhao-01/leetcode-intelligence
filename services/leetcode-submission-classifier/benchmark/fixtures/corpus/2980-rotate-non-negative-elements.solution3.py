# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: rotate-non-negative-elements
# source_path: LeetCode-Solutions-master/Python/rotate-non-negative-elements.py
# solution_class: Solution3
# submission_id: e3823019170be1e84f824eaba8670471a2c4ac43
# seed: 3122507908

# Time:  O(n)
# Space: O(n)

# array

class Solution3(object):
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
            nums[:] = nums[k:]+nums[:k]

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