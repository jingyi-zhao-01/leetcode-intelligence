# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-complement
# source_path: LeetCode-Solutions-master/Python/number-complement.py
# solution_class: Solution
# submission_id: 4d3c6d2424298bf4bdba16e63e9ced379d5676fa
# seed: 868976268

# Time:  O(1)
# Space: O(1)

class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        return 2 ** (len(bin(num)) - 2) - 1 - num