# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: factorial-trailing-zeroes
# source_path: LeetCode-Solutions-master/Python/factorial-trailing-zeroes.py
# solution_class: Solution
# submission_id: 167e8ff7bbc15b09bf1363ca37ef6bc7e81b6bb1
# seed: 1726245612

# Time:  O(logn) = O(1)
# Space: O(1)

class Solution(object):
    # @return an integer
    def trailingZeroes(self, n):
        result = 0
        while n > 0:
            result += n / 5
            n /= 5
        return result