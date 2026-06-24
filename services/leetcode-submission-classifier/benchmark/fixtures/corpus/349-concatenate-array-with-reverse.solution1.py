# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: concatenate-array-with-reverse
# source_path: LeetCode-Solutions-master/Python/concatenate-array-with-reverse.py
# solution_class: Solution
# submission_id: bd4c190b7fd4aae33a1224a61f24d21099a83ce8
# seed: 561517321

# Time:  O(n)
# Space: O(1)

# array

class Solution(object):
    def concatWithReverse(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.extend(reversed(nums))
        return nums