# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: mirror-distance-of-an-integer
# source_path: LeetCode-Solutions-master/Python/mirror-distance-of-an-integer.py
# solution_class: Solution
# submission_id: 5e3efcbaa48a45576ceb699bf1bea576953058f7
# seed: 3941339057

# Time:  O(logn)
# Space: O(1)

# math

class Solution(object):
    def mirrorDistance(self, n):
        """
        :type n: int
        :rtype: int
        """
        def reverse(n):
            result = 0
            while n:
                n, r = divmod(n, 10)
                result = result*10+r
            return result

        return abs(n-reverse(n))