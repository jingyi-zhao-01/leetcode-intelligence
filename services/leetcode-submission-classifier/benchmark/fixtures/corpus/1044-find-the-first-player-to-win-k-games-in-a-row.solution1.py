# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-the-first-player-to-win-k-games-in-a-row
# source_path: LeetCode-Solutions-master/Python/find-the-first-player-to-win-k-games-in-a-row.py
# solution_class: Solution
# submission_id: 342e59dc2064928ab5e7341b067fc39d8c5914b2
# seed: 1302113195

# Time:  O(n)
# Space: O(1)

# simulation

class Solution(object):
    def findWinningPlayer(self, skills, k):
        """
        :type skills: List[int]
        :type k: int
        :rtype: int
        """
        result = cnt = 0
        for i in range(1, len(skills)):
            if skills[result] < skills[i]:
                result = i
                cnt = 0
            cnt += 1
            if cnt == k:
                return result
        return result