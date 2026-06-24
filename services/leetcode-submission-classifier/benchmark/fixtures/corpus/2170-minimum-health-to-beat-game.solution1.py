# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-health-to-beat-game
# source_path: LeetCode-Solutions-master/Python/minimum-health-to-beat-game.py
# solution_class: Solution
# submission_id: 371abb9850f15749cb45907b77c5ccca0fcc17c4
# seed: 3971899630

# Time:  O(n)
# Space: O(1)

# greedy

class Solution(object):
    def minimumHealth(self, damage, armor):
        """
        :type damage: List[int]
        :type armor: int
        :rtype: int
        """
        return sum(damage)-min(max(damage), armor)+1