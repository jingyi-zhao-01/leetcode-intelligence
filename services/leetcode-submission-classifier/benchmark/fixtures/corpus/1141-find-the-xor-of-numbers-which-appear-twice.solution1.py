# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-the-xor-of-numbers-which-appear-twice
# source_path: LeetCode-Solutions-master/Python/find-the-xor-of-numbers-which-appear-twice.py
# solution_class: Solution
# submission_id: 2be7dce9181b7e48fe8555c766179836f1fa0e99
# seed: 136071793

# Time:  O(n)
# Space: O(n)

# hash table

class Solution(object):
    def duplicateNumbersXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return reduce(lambda x, y: x^y, nums, 0)^reduce(lambda x, y: x^y, set(nums), 0)