# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: fill-a-special-grid
# source_path: LeetCode-Solutions-master/Python/fill-a-special-grid.py
# solution_class: Solution2
# submission_id: 446b845c815a8f698727967c593f3a0304f7ee5d
# seed: 692070028

# Time:  O(4^n)
# Space: O(1)

# array

class Solution2(object):
    def specialGrid(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        def divide_and_conquer(l, r, c):
            if l == 1:
                result[r][c] = idx[0]
                idx[0] += 1
                return
            l >>= 1
            for dr, dc in ((0, l), (l, 0), (0, -l), (-l, 0)):
                r, c = r+dr, c+dc
                divide_and_conquer(l, r, c)

        total = 1<<n
        result = [[0]*total for _ in xrange(total)]
        idx = [0]
        divide_and_conquer(total, 0, 0)
        return result