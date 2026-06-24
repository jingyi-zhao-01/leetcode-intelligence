# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: falling-squares
# source_path: LeetCode-Solutions-master/Python/falling-squares.py
# solution_class: Solution2
# submission_id: 8a77435b48bf3c55794f4f98d96466226b0b30c6
# seed: 3211865971

# Time:  O(n^2), could be improved to O(nlogn) in cpp by ordered map (bst)
# Space: O(n)

import bisect

class Solution2(object):
    def fallingSquares(self, positions):
        index = set()
        for left, size in positions:
            index.add(left)
            index.add(left+size-1)
        index = sorted(list(index))
        tree = SegmentTree(len(index), max, max, 0)
        # tree = SegmentTree2([0]*len(index), max, max, 0)
        max_height = 0
        result = []
        for left, size in positions:
            L, R = bisect.bisect_left(index, left), bisect.bisect_left(index, left+size-1)
            h = tree.query(L, R) + size
            tree.update(L, R, h)
            max_height = max(max_height, h)
            result.append(max_height)
        return result