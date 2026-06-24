# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: bitwise-and-of-numbers-range
# source_path: LeetCode-Solutions-master/Python/bitwise-and-of-numbers-range.py
# solution_class: Solution
# submission_id: 4ec6ce993bdd8394666001004b6a6b1590372a64
# seed: 2233554697

# Time:  O(1)
# Space: O(1)

class Solution(object):
    # @param m, an integer
    # @param n, an integer
    # @return an integer
    def rangeBitwiseAnd(self, m, n):
        while m < n:
            n &= n - 1
        return n