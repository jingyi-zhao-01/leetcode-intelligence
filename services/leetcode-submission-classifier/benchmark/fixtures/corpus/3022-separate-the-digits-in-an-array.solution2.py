# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: separate-the-digits-in-an-array
# source_path: LeetCode-Solutions-master/Python/separate-the-digits-in-an-array.py
# solution_class: Solution2
# submission_id: 2fc96bbc878f4da77db585300372bcf65fb82148
# seed: 345628318

# Time:  O(n * logr)
# Space: O(1)

# array

class Solution2(object):
    def separateDigits(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return [int(c) for x in nums for c in str(x)]