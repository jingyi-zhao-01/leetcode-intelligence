# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-69-number
# source_path: LeetCode-Solutions-master/Python/maximum-69-number.py
# solution_class: Solution
# submission_id: 582f20a96366a799dfd18e8ed7cc213fbb5fec5c
# seed: 3379798625

# Time:  O(logn)
# Space: O(1)

class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        curr, base, change = num, 3, 0
        while curr:
            if curr%10 == 6:
                change = base
            base *= 10
            curr //= 10
        return num+change