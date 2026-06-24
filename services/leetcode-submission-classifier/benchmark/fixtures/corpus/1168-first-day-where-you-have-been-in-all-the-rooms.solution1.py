# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: first-day-where-you-have-been-in-all-the-rooms
# source_path: LeetCode-Solutions-master/Python/first-day-where-you-have-been-in-all-the-rooms.py
# solution_class: Solution
# submission_id: 9d9c37da278d96f16b9d9645af67800aa869cb43
# seed: 4223653927

# Time:  O(n)
# Space: O(n)

class Solution(object):
    def firstDayBeenInAllRooms(self, nextVisit):
        """
        :type nextVisit: List[int]
        :rtype: int
        """
        MOD = 10**9+7

        dp = [0]*len(nextVisit)
        for i in xrange(1, len(dp)):
            dp[i] = (dp[i-1]+1+(dp[i-1]-dp[nextVisit[i-1]])+1)%MOD
        return dp[-1]