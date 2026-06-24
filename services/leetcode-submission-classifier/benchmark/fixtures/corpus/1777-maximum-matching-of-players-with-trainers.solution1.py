# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-matching-of-players-with-trainers
# source_path: LeetCode-Solutions-master/Python/maximum-matching-of-players-with-trainers.py
# solution_class: Solution
# submission_id: 3a01f623190cd518a17607f463b10163c56580f7
# seed: 266576680

# Time:  O(nlogn + mlogm)
# Space: O(1)

# greedy, sort

class Solution(object):
    def matchPlayersAndTrainers(self, players, trainers):
        """
        :type players: List[int]
        :type trainers: List[int]
        :rtype: int
        """
        players.sort()
        trainers.sort()
        result = 0
        for x in trainers:
            if players[result] > x:
                continue
            result += 1
            if result == len(players):
                break
        return result