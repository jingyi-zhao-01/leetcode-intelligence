# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: sort-even-and-odd-indices-independently
# source_path: LeetCode-Solutions-master/Python/sort-even-and-odd-indices-independently.py
# solution_class: Solution3
# submission_id: df1007e4fd60d5f8c79faa164fc641289b072d46
# seed: 1074816967

# Time:  O(n)
# Space: O(c), c is the max of nums

# counting sort, inplace solution

class Solution3(object):
    def sortEvenOdd(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums[::2], nums[1::2] = sorted(nums[::2]), sorted(nums[1::2], reverse=True)
        return nums