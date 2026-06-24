# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: smallest-number-with-all-set-bits
# source_path: LeetCode-Solutions-master/Python/smallest-number-with-all-set-bits.py
# solution_class: Solution
# submission_id: 439537d45ddcb6314386674f132142076667f349
# seed: 1661016092

# Time:  O(1)
# Space: O(1)

# bit manipulation

class Solution(object):
    def smallestNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        return (1<<n.bit_length())-1