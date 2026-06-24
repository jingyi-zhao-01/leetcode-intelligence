# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: power-of-two
# source_path: LeetCode-Solutions-master/Python/power-of-two.py
# solution_class: Solution
# submission_id: 8e88e902d3242ee92cb9b6d5a75954a1c1f05056
# seed: 2344382883

# Time:  O(1)
# Space: O(1)

class Solution(object):
    # @param {integer} n
    # @return {boolean}
    def isPowerOfTwo(self, n):
        return n > 0 and (n & (n - 1)) == 0