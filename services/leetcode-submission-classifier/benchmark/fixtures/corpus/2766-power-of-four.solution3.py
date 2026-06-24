# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: power-of-four
# source_path: LeetCode-Solutions-master/Python/power-of-four.py
# solution_class: Solution3
# submission_id: f78ef154b3edf26e04ed5718f07cd60257b93ee6
# seed: 1144518084

# Time:  O(1)
# Space: O(1)

class Solution3(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        num = bin(num)
        return True if num[2:].startswith('1') and len(num[2:]) == num.count('0') and num.count('0') % 2 and '-' not in num else False