# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-removals-to-balance-array
# source_path: LeetCode-Solutions-master/Python/minimum-removals-to-balance-array.py
# solution_class: Solution2
# submission_id: 4ee620e7bdf5d41194b44f7256efdcf57da61df3
# seed: 1100763847

# Time:  O(nlogn)
# Space: O(1)

# sort, two pointers

class Solution2(object):
    def minRemoval(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        result = left = 0
        for right in xrange(len(nums)):
            while nums[left]*k < nums[right]:
                left += 1
            result = max(result, right-left+1)
        return len(nums)-result