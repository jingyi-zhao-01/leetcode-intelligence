# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: build-array-from-permutation
# source_path: LeetCode-Solutions-master/Python/build-array-from-permutation.py
# solution_class: Solution
# submission_id: e91dbc7b32129e96a2e3b817fcc8da3b63d429e1
# seed: 1612117311

# Time:  O(n)
# Space: O(1)

# inplace solution

class Solution(object):
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in xrange(len(nums)):
            prev, curr = i, nums[i]
            while curr >= 0 and curr != i:
                nums[prev], nums[curr] = ~nums[curr], ~nums[prev] if prev == i else nums[prev]
                prev, curr = curr, ~nums[prev]
        for i in xrange(len(nums)):
            if nums[i] < 0:
                nums[i] = ~nums[i]
        return nums