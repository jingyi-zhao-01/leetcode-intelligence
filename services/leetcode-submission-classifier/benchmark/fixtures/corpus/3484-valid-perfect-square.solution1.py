# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: valid-perfect-square
# source_path: LeetCode-Solutions-master/Python/valid-perfect-square.py
# solution_class: Solution
# submission_id: d07f5e5cf6b88432dac66307a0414408bb46c2c7
# seed: 3964670802

# Time:  O(logn)
# Space: O(1)

class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        left, right = 1, num
        while left <= right:
            mid = left + (right - left) // 2
            if mid >= num / mid:
                right = mid - 1
            else:
                left = mid + 1
        return left == num / left and num % left == 0