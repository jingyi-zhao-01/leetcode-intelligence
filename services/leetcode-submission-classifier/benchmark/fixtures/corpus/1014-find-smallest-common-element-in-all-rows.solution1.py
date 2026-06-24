# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-smallest-common-element-in-all-rows
# source_path: LeetCode-Solutions-master/Python/find-smallest-common-element-in-all-rows.py
# solution_class: Solution
# submission_id: a10a06cc9b7831303faceded451d3f1417ec7b0e
# seed: 797354731

# Time:  O(m * n)
# Space: O(n)

class Solution(object):
    def smallestCommonElement(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        # values could be duplicated in each row
        intersections = set(mat[0])
        for i in xrange(1, len(mat)):
            intersections &= set(mat[i])
            if not intersections:
                return -1
        return min(intersections)