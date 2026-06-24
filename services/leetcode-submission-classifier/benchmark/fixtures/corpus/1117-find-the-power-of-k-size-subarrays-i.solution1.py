# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-the-power-of-k-size-subarrays-i
# source_path: LeetCode-Solutions-master/Python/find-the-power-of-k-size-subarrays-i.py
# solution_class: Solution
# submission_id: 4a054d463ddbac145736c600aa506956aa4433e4
# seed: 1327510565

# Time:  O(n)
# Space: O(1)

# two pointers, sliding window

class Solution(object):
    def resultsArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        result = [-1]*(len(nums)-k+1)
        left = 0
        for right in xrange(len(nums)):
            if nums[right]-nums[left] != right-left:
                left = right
            if right-left+1 == k:
                result[left] = nums[right]
                left += 1
        return result