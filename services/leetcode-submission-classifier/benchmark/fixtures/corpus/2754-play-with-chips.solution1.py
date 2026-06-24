# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: play-with-chips
# source_path: LeetCode-Solutions-master/Python/play-with-chips.py
# solution_class: Solution
# submission_id: a4a50f387999263fdffb758f847413c66caa6bc9
# seed: 2155868521

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def minCostToMoveChips(self, chips):
        """
        :type chips: List[int]
        :rtype: int
        """
        count = [0]*2
        for p in chips:
            count[p%2] += 1
        return min(count)