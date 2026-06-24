# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: create-grid-with-exactly-one-path
# source_path: LeetCode-Solutions-master/Python/create-grid-with-exactly-one-path.py
# solution_class: Solution
# submission_id: a92f0dcce0afada20fc9a11480110e31e3881749
# seed: 3743070410

# Time:  O(m * n)
# Space: O(1)

# array

class Solution(object):
    def createGrid(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: List[str]
        """
        result = [['#']*n for _ in xrange(m)]
        for j in xrange(n):
            result[0][j] = '.'
        for i in xrange(m):
            result[i][-1] = '.'
        return ["".join(row) for row in result]