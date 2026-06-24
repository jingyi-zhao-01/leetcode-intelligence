# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-array-end
# source_path: LeetCode-Solutions-master/Python/minimum-array-end.py
# solution_class: Solution
# submission_id: 69690f4b51caaa34a8348d3fb7e257641d9b60c2
# seed: 1960613632

# Time:  O(logn)
# Space: O(1)

# bit manipulation

class Solution(object):
    def minEnd(self, n, x):
        """
        :type n: int
        :type x: int
        :rtype: int
        """
        n -= 1
        base_n = base_x = 1
        while base_n <= n:
            if (x&base_x) == 0:
                if n&base_n:
                    x |= base_x
                base_n <<= 1
            base_x <<= 1
        return x