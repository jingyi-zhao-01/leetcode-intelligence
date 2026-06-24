# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-the-degree-of-each-vertex
# source_path: LeetCode-Solutions-master/Python/find-the-degree-of-each-vertex.py
# solution_class: Solution
# submission_id: 81ecbe9b93b571c9a9ec1e9a63bb474b59e64a4b
# seed: 239637543

# Time:  O(n * m)
# Space: O(1)

# array

class Solution(object):
    def findDegrees(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        return [sum(row) for row in matrix]