# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: bitwise-and-of-numbers-range
# source_path: LeetCode-Solutions-master/Python/bitwise-and-of-numbers-range.py
# solution_class: Solution2
# submission_id: 5a8bf94a40a88b5667806574cb342307647566fc
# seed: 2755113865

# Time:  O(1)
# Space: O(1)

class Solution2(object):
    # @param m, an integer
    # @param n, an integer
    # @return an integer
    def rangeBitwiseAnd(self, m, n):
        i, diff = 0, n-m
        while diff:
            diff >>= 1
            i += 1
        return n & m >> i << i