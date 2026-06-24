# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: reverse-k-subarrays
# source_path: LeetCode-Solutions-master/Python/reverse-k-subarrays.py
# solution_class: Solution
# submission_id: acc3791487fbe282e58459fa58fc387c5bcfa585
# seed: 2603011944

# Time:  O(n)
# Space: O(1)

# array

class Solution(object):
    def reverseSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        def reverse(left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        l = len(nums)//k
        for i in xrange(0, len(nums), l):
            reverse(i, i+l-1)
        return nums