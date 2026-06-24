# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: color-the-triangle-red
# source_path: LeetCode-Solutions-master/Python/color-the-triangle-red.py
# solution_class: Solution
# submission_id: 32f109219b7e5d9263494275d7e32afd7a11962e
# seed: 4042898690

# Time:  O(n^2)
# Space: O(1)

# constructive algorithms

class Solution(object):
    def colorRed(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        result = [[1, 1]]
        for i in xrange(2, n+1):
            if i%2 == n%2:
                result.extend([i, j] for j in xrange((1 if i%4 == n%4 else 3), 2*i, 2))
            else:
                result.append([i, (2 if i%4 == (n-1)%4 else 1)])
        return result