# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-monobit-integers
# source_path: LeetCode-Solutions-master/Python/count-monobit-integers.py
# solution_class: Solution
# submission_id: 1827046a1622b58e130ef8f988340a4a3f6c99f8
# seed: 3517710426

# Time:  O(logn)
# Space: O(1)

# bitmasks

class Solution(object):
    def countMonobit(self, n):
        """
        :type n: int
        :rtype: int
        """
        return (n+1).bit_length()