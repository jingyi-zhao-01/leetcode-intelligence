# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: frequency-of-the-most-frequent-element
# source_path: LeetCode-Solutions-master/Python/frequency-of-the-most-frequent-element.py
# solution_class: Solution
# submission_id: 3829d652448fa730d031e07ef0b18d9bca54aeb4
# seed: 2641286998

# Time:  O(nlogn)
# Space: O(n)

class Solution(object):
    def maxFrequency(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left = 0
        nums.sort()
        for right in xrange(len(nums)):
            k += nums[right]
            if k < nums[right]*(right-left+1):
                k -= nums[left]
                left += 1
        return right-left+1