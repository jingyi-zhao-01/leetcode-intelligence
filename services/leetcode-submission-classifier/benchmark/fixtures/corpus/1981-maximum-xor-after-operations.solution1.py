# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-xor-after-operations
# source_path: LeetCode-Solutions-master/Python/maximum-xor-after-operations.py
# solution_class: Solution
# submission_id: 8938ff2078a608053b5cd6aeaa0b2725b9ef6ce9
# seed: 2942427483

# Time:  O(n)
# Space: O(1)

# bit manipulation

class Solution(object):
    def maximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return reduce(lambda x, y: x|y, nums)