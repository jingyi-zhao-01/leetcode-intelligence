# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: sqrtx
# source_path: LeetCode-Solutions-master/Python/sqrtx.py
# solution_class: Solution
# submission_id: cccbf4d7dfe371f27c3edf84450b4b3b52c15ba4
# seed: 4292491215

# Time:  O(logn)
# Space: O(1)

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 2:
            return x

        left, right = 1, x // 2
        while left <= right:
            mid = left + (right - left) // 2
            if mid > x / mid:
                right = mid - 1
            else:
                left = mid + 1

        return left - 1