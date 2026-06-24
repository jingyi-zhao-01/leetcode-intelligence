# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-all-good-indices
# source_path: LeetCode-Solutions-master/Python/find-all-good-indices.py
# solution_class: Solution
# submission_id: dcf2d87fe924a048451554692b20c7bab62e43f6
# seed: 3650978475

# Time:  O(n)
# Space: O(n)

# prefix sum

class Solution(object):
    def goodIndices(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        left = [1]*len(nums)
        for i in xrange(1, len(nums)-1):
            if nums[i] <= nums[i-1]:
                left[i] = left[i-1]+1
        right = [1]*len(nums)
        for i in reversed(xrange(1, len(nums)-1)):
            if nums[i] <= nums[i+1]:
                right[i] = right[i+1]+1
        return [i for i in xrange(k, len(nums)-k) if min(left[i-1], right[i+1]) >= k]