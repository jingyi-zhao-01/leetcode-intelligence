# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-69-number
# source_path: LeetCode-Solutions-master/Python/maximum-69-number.py
# solution_class: Solution2
# submission_id: 81365ce80b46ee1125be62f9b9a52ec09d03d6cc
# seed: 254562553

# Time:  O(logn)
# Space: O(1)

class Solution2(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        return int(str(num).replace('6', '9', 1))