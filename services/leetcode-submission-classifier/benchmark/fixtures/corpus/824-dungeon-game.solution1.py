# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: dungeon-game
# source_path: LeetCode-Solutions-master/Python/dungeon-game.py
# solution_class: Solution
# submission_id: 2ec9d09926d832032c423fc4ec294864e101a9c0
# seed: 2653395084

# Time:  O(m * n)
# Space: O(m + n)

class Solution(object):
    # @param dungeon, a list of lists of integers
    # @return a integer
    def calculateMinimumHP(self, dungeon):
        DP = [float("inf") for _ in dungeon[0]]
        DP[-1] = 1

        for i in reversed(xrange(len(dungeon))):
            DP[-1] = max(DP[-1] - dungeon[i][-1], 1)
            for j in reversed(xrange(len(dungeon[i]) - 1)):
                min_HP_on_exit = min(DP[j], DP[j + 1])
                DP[j] = max(min_HP_on_exit - dungeon[i][j], 1)

        return DP[0]