# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-height-of-a-triangle
# source_path: LeetCode-Solutions-master/Python/maximum-height-of-a-triangle.py
# solution_class: Solution2
# submission_id: 7103580dcfd2f9c9db8a9d031041f89f16b81004
# seed: 3551699248

# Time:  O(logn)
# Space: O(1)

# math

class Solution2(object):
    def maxHeightOfTriangle(self, red, blue):
        """
        :type red: int
        :type blue: int
        :rtype: int
        """
        def f(x, y):
            h = 0
            while x >= h+1:
                h += 1
                x -= h
                x, y = y, x
            return h

        return max(f(red, blue), f(blue, red))