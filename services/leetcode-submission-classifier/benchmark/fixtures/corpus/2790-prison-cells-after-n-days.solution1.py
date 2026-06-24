# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: prison-cells-after-n-days
# source_path: LeetCode-Solutions-master/Python/prison-cells-after-n-days.py
# solution_class: Solution
# submission_id: 19a8c2d94384d0b7a62e92306d5871855521173c
# seed: 2687543276

# Time:  O(1)
# Space: O(1)

class Solution(object):
    def prisonAfterNDays(self, cells, N):
        """
        :type cells: List[int]
        :type N: int
        :rtype: List[int]
        """
        N -= max(N-1, 0) // 14 * 14  # 14 is got from Solution2
        for i in xrange(N):
            cells = [0] + [cells[i-1] ^ cells[i+1] ^ 1 for i in xrange(1, 7)] + [0]
        return cells