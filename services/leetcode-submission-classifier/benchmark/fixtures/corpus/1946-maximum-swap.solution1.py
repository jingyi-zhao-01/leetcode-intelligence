# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-swap
# source_path: LeetCode-Solutions-master/Python/maximum-swap.py
# solution_class: Solution
# submission_id: a871483ea87d883de73520cd036bd35d92e9ddd9
# seed: 4199594580

# Time:  O(logn), logn is the length of the number string
# Space: O(logn)

class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        digits = list(str(num))
        left, right = 0, 0
        max_idx = len(digits)-1
        for i in reversed(xrange(len(digits))):
            if digits[i] > digits[max_idx]:
                max_idx = i
            elif digits[max_idx] > digits[i]:
                left, right = i, max_idx
        digits[left], digits[right] = digits[right], digits[left]
        return int("".join(digits))