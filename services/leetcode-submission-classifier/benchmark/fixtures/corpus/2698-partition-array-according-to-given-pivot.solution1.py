# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: partition-array-according-to-given-pivot
# source_path: LeetCode-Solutions-master/Python/partition-array-according-to-given-pivot.py
# solution_class: Solution
# submission_id: 3a86d8f217b3575c6117b078879f4328f7d48169
# seed: 156428843

# Time:  O(n)
# Space: O(n)

# two pointers

class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        result = [pivot]*len(nums)
        left, right = 0, len(nums)-sum(x > pivot for x in nums)
        for x in nums:
            if x < pivot:
                result[left] = x
                left += 1
            elif x > pivot:
                result[right] = x
                right += 1
        return result