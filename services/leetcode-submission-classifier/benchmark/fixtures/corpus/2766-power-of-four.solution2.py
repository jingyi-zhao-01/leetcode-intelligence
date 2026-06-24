# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: power-of-four
# source_path: LeetCode-Solutions-master/Python/power-of-four.py
# solution_class: Solution2
# submission_id: 7faa6b0c3aa54942cf7b30cb0dbe9a5021e513af
# seed: 2962667751

# Time:  O(1)
# Space: O(1)

class Solution2(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        while num and not (num & 0b11):
            num >>= 2
        return (num == 1)