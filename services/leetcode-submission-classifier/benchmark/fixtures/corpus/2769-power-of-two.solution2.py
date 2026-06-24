# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: power-of-two
# source_path: LeetCode-Solutions-master/Python/power-of-two.py
# solution_class: Solution2
# submission_id: 857deba2cf6eceb49d91e441790f25d21de10e07
# seed: 2455159670

# Time:  O(1)
# Space: O(1)

class Solution2(object):
    # @param {integer} n
    # @return {boolean}
    def isPowerOfTwo(self, n):
        return n > 0 and (n & ~-n) == 0