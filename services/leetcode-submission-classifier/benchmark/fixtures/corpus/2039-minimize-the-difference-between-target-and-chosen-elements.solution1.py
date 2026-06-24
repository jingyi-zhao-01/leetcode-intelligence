# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimize-the-difference-between-target-and-chosen-elements
# source_path: LeetCode-Solutions-master/Python/minimize-the-difference-between-target-and-chosen-elements.py
# solution_class: Solution
# submission_id: 417f616749f647649fcfaa0c6e0c7258f5994511
# seed: 762531949

# Time:  O(t * m * n), t is target
# Space: O(t)

class Solution(object):
    def minimizeTheDifference(self, mat, target):
        """
        :type mat: List[List[int]]
        :type target: int
        :rtype: int
        """
        chosen_min = sum(min(row) for row in mat)
        if chosen_min >= target:
            return chosen_min-target
        dp = {0}
        for row in mat:
            dp = {total+x for total in dp for x in row if (total+x)-target < target-chosen_min}
        return min(abs(target-total) for total in dp)