# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-height-of-a-triangle
# source_path: LeetCode-Solutions-master/Python/maximum-height-of-a-triangle.py
# solution_class: Solution
# submission_id: 5f893cfdf697ad3bddbbef3cb88334ce1098c6d1
# seed: 1660829939

# Time:  O(logn)
# Space: O(1)

# math

class Solution(object):
    def maxHeightOfTriangle(self, red, blue):
        """
        :type red: int
        :type blue: int
        :rtype: int
        """
        def f(x, y):
            # odd level:
            # (1+h)*((1+h)//2)//2 <= x
            # => h <= int(2*x**0.5)-1
            # even level:
            # (2+h)*(h//2)//2 <= y
            # => h <= int((4*y+1)**0.5)-1
            a, b = int(2*x**0.5)-1, int((4*y+1)**0.5)-1
            return min(a, b)+int(a != b)
        
        return max(f(red, blue), f(blue, red))