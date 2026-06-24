# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: bitwise-or-of-even-numbers-in-an-array
# source_path: LeetCode-Solutions-master/Python/bitwise-or-of-even-numbers-in-an-array.py
# solution_class: Solution
# submission_id: d73de4c97e635b2c8d3a23a4cc2c5a538eeaa22b
# seed: 4097162623

# Time:  O(n)
# Space: O(1)

# array

class Solution(object):
    def evenNumberBitwiseORs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return reduce(lambda total, x: total|(x if x%2 == 0 else 0), nums, 0)