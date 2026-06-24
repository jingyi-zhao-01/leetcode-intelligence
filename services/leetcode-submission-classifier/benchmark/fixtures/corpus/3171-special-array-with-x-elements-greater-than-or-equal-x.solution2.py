# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: special-array-with-x-elements-greater-than-or-equal-x
# source_path: LeetCode-Solutions-master/Python/special-array-with-x-elements-greater-than-or-equal-x.py
# solution_class: Solution2
# submission_id: 84518e36f5c9afdb172938ebc899098d98333964
# seed: 1018279892

# Time:  O(n)
# Space: O(1)

# counting sort solution

class Solution2(object):
    def specialArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        MAX_NUM = 1000
        def inplace_counting_sort(nums, reverse=False):  # Time: O(n)
            count = [0]*(MAX_NUM+1)
            for num in nums:
                count[num] += 1
            for i in xrange(1, len(count)):
                count[i] += count[i-1]
            for i in reversed(xrange(len(nums))):  # inplace but unstable sort
                while nums[i] >= 0:
                    count[nums[i]] -= 1
                    j = count[nums[i]]
                    nums[i], nums[j] = nums[j], ~nums[i]
            for i in xrange(len(nums)):
                nums[i] = ~nums[i]  # restore values
            if reverse:  # unstable sort
                nums.reverse()
    
        inplace_counting_sort(nums, reverse=True)
        left, right = 0, len(nums)-1
        while left <= right:  # Time: O(logn)
            mid = left + (right-left)//2
            if nums[mid] <= mid:
                right = mid-1
            else:
                left = mid+1
        return -1 if left < len(nums) and nums[left] == left else left