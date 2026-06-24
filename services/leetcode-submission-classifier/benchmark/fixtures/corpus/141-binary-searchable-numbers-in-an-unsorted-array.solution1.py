# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: binary-searchable-numbers-in-an-unsorted-array
# source_path: LeetCode-Solutions-master/Python/binary-searchable-numbers-in-an-unsorted-array.py
# solution_class: Solution
# submission_id: fc5fac06e4d5a7239c89479f2b51a559c4208e56
# seed: 3880385194


# Time:  O(n)
# Space: O(n)

class Solution(object):
    def binarySearchableNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        right = [float("inf")]*(len(nums)+1)
        for i in reversed(xrange(1, len(nums)+1)):
            right[i-1] = min(right[i], nums[i-1])
        result, left = set(), float("-inf")
        for i in xrange(len(nums)):
            if left <= nums[i] <= right[i+1]:
                result.add(nums[i])
            left = max(left, nums[i])
        return len(result)