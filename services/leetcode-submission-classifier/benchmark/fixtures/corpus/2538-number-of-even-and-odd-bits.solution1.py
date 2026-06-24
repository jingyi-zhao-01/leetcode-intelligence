# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-even-and-odd-bits
# source_path: LeetCode-Solutions-master/Python/number-of-even-and-odd-bits.py
# solution_class: Solution
# submission_id: 44309a798aec6b3969dfe49461744986b8ab3a3e
# seed: 3989586475

# Time:  O(1)
# Space: O(1)

# bit manipulation

class Solution(object):
    def evenOddBit(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        def popcount(x):
            return bin(x)[2:].count('1')

        return [popcount(n&0b0101010101), popcount(n&0b1010101010)]