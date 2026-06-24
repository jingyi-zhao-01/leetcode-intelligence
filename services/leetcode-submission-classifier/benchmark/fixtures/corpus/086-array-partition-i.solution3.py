# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: array-partition-i
# source_path: LeetCode-Solutions-master/Python/array-partition-i.py
# solution_class: Solution3
# submission_id: 0f7c1d7c8425073f48829b5670e3769c6c26d570
# seed: 2521997409

# Time:  O(r), r is the range size of the integers
# Space: O(r)

class Solution3(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        return sum([nums[i] for i in range(0, len(nums), 2)])