# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: falling-squares
# source_path: LeetCode-Solutions-master/Python/falling-squares.py
# solution_class: Solution4
# submission_id: 006085cdbee7ac6b0214e063645535a908deaa03
# seed: 1417683057

# Time:  O(n^2), could be improved to O(nlogn) in cpp by ordered map (bst)
# Space: O(n)

import bisect

class Solution4(object):
    def fallingSquares(self, positions):
        """
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        heights = [0] * len(positions)
        for i in xrange(len(positions)):
            left_i, size_i = positions[i]
            right_i = left_i + size_i
            heights[i] += size_i
            for j in xrange(i+1, len(positions)):
                left_j, size_j = positions[j]
                right_j = left_j + size_j
                if left_j < right_i and left_i < right_j:  # intersect
                    heights[j] = max(heights[j], heights[i])

        result = []
        for height in heights:
            result.append(max(result[-1], height) if result else height)
        return result