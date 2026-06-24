# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: falling-squares
# source_path: LeetCode-Solutions-master/Python/falling-squares.py
# solution_class: Solution
# submission_id: 90b323f4ca66f8fbc879acbb587e94658bb9b748
# seed: 3730118970

# Time:  O(n^2), could be improved to O(nlogn) in cpp by ordered map (bst)
# Space: O(n)

import bisect

class Solution(object):
    def fallingSquares(self, positions):
        result = []
        pos = [-1]
        heights = [0]
        maxH = 0
        for left, side in positions:
            l = bisect.bisect_right(pos, left)
            r = bisect.bisect_left(pos, left+side)
            high = max(heights[l-1:r] or [0]) + side
            pos[l:r] = [left, left+side]         # Time: O(n)
            heights[l:r] = [high, heights[r-1]]  # Time: O(n)
            maxH = max(maxH, high)
            result.append(maxH)
        return result