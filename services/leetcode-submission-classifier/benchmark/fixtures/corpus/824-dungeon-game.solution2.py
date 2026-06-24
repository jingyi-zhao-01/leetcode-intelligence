# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: dungeon-game
# source_path: LeetCode-Solutions-master/Python/dungeon-game.py
# solution_class: Solution2
# submission_id: 5f7b622a7d9ac466deb53c89d9fb5ed1629d2515
# seed: 2893911708

# Time:  O(m * n)
# Space: O(m + n)

class Solution2(object):
    # @param dungeon, a list of lists of integers
    # @return a integer
    def calculateMinimumHP(self, dungeon):
        maximum_loses = 0
        for rooms in dungeon:
            for room in rooms:
                if room < 0:
                    maximum_loses += abs(room)

        return self.binarySearch(dungeon, maximum_loses)

    def binarySearch(self, dungeon, maximum_loses):
        start, end = 1, maximum_loses + 1
        result = 0
        while start < end:
            mid = start + (end - start) / 2
            if self.DP(dungeon, mid):
                end = mid
            else:
                start = mid + 1
        return start

    def DP(self, dungeon, HP):
        remain_HP = [0 for _ in dungeon[0]]
        remain_HP[0] = HP + dungeon[0][0]
        for j in xrange(1, len(remain_HP)):
            if remain_HP[j - 1] > 0:
                remain_HP[j] = max(remain_HP[j - 1] + dungeon[0][j], 0)

        for i in xrange(1, len(dungeon)):
            if remain_HP[0] > 0:
                remain_HP[0] = max(remain_HP[0] + dungeon[i][0], 0)
            else:
                remain_HP[0] = 0

            for j in xrange(1, len(remain_HP)):
                remain = 0
                if remain_HP[j - 1] > 0:
                    remain = max(remain_HP[j - 1] + dungeon[i][j], remain)
                if remain_HP[j] > 0:
                    remain = max(remain_HP[j] + dungeon[i][j], remain)
                remain_HP[j] = remain

        return remain_HP[-1] > 0