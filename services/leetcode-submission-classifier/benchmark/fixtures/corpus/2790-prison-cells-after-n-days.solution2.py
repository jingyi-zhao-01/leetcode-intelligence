# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: prison-cells-after-n-days
# source_path: LeetCode-Solutions-master/Python/prison-cells-after-n-days.py
# solution_class: Solution2
# submission_id: a04ca741463192edf2b4d2c44bf90da4fddabe34
# seed: 3223584903

# Time:  O(1)
# Space: O(1)

class Solution2(object):
    def prisonAfterNDays(self, cells, N):
        """
        :type cells: List[int]
        :type N: int
        :rtype: List[int]
        """
        cells = tuple(cells)
        lookup = {}
        while N:
            lookup[cells] = N
            N -= 1
            cells = tuple([0] + [cells[i - 1] ^ cells[i + 1] ^ 1 for i in xrange(1, 7)] + [0])
            if cells in lookup:
                assert(lookup[cells] - N in (1, 7, 14))
                N %= lookup[cells] - N
                break

        while N:
            N -= 1
            cells = tuple([0] + [cells[i - 1] ^ cells[i + 1] ^ 1 for i in xrange(1, 7)] + [0])
        return list(cells)