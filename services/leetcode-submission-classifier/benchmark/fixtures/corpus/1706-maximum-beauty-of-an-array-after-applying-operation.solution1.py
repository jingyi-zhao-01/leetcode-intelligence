# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-beauty-of-an-array-after-applying-operation
# source_path: LeetCode-Solutions-master/Python/maximum-beauty-of-an-array-after-applying-operation.py
# solution_class: Solution
# submission_id: 151307737a9315f0999aec9a73466079096a8aa8
# seed: 199911325

# Time:  O(nlogn)
# Space: O(1)

# sort, two pointers, sliding window

class Solution(object):
    def maximumBeauty(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        left = 0
        for right in xrange(len(nums)):
            if nums[right]-nums[left] > k*2:
                left += 1
        return right-left+1