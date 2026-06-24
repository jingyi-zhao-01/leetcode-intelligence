# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-cost-for-cutting-cake-i
# source_path: LeetCode-Solutions-master/Python/minimum-cost-for-cutting-cake-i.py
# solution_class: Solution
# submission_id: 713937234b9fd3888c3f492b60c2383906299fbc
# seed: 2693022251

# Time:  O(mlogm + nlogn)
# Space: O(1)

# sort, greedy

class Solution(object):
    def minimumCost(self, m, n, horizontalCut, verticalCut):
        """
        :type m: int
        :type n: int
        :type horizontalCut: List[int]
        :type verticalCut: List[int]
        :rtype: int
        """
        horizontalCut.sort()
        verticalCut.sort()
        result = 0
        cnt_h = cnt_v = 1
        while horizontalCut or verticalCut:
            if not verticalCut or (horizontalCut and horizontalCut[-1] > verticalCut[-1]):
                result += horizontalCut.pop()*cnt_h
                cnt_v += 1
            else:
                result += verticalCut.pop()*cnt_v
                cnt_h += 1
        return result