# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-number-that-makes-result-of-bitwise-and-zero
# source_path: LeetCode-Solutions-master/Python/maximum-number-that-makes-result-of-bitwise-and-zero.py
# solution_class: Solution
# submission_id: 4b76439f6f68b7bbb8ec76c3e20cf5f3557b0fae
# seed: 3194167939

# Time:  O(1)
# Space: O(1)

# bit manipulation

class Solution(object):
    def maxNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        return (1<<(n.bit_length()-1))-1