# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-the-width-of-columns-of-a-grid
# source_path: LeetCode-Solutions-master/Python/find-the-width-of-columns-of-a-grid.py
# solution_class: Solution3
# submission_id: 7ed85cbe37b75ff810758d9cd0665ba6cf051094
# seed: 3441829081

# Time:  O(m * n)
# Space: O(1)

# array

class Solution3(object):
    def findColumnWidth(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        return [max(len(str(x)) for x in col) for col in itertools.izip(*grid)]