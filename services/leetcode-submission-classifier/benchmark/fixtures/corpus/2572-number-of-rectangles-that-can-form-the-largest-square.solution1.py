# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-rectangles-that-can-form-the-largest-square
# source_path: LeetCode-Solutions-master/Python/number-of-rectangles-that-can-form-the-largest-square.py
# solution_class: Solution
# submission_id: 1443db23bf9c5278106068a42494f7e4fd2390c9
# seed: 3254195733

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def countGoodRectangles(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: int
        """
        result = mx = 0
        for l, w in rectangles:
            side = min(l, w)
            if side > mx:
                result, mx = 1, side
            elif side == mx:
                result += 1
        return result