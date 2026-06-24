# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-walls-destroyed-by-robots
# source_path: LeetCode-Solutions-master/Python/maximum-walls-destroyed-by-robots.py
# solution_class: Solution
# submission_id: f1a523a79e246614e75ca463faf0a46a471f6d16
# seed: 1243592196

# Time:  O(nlogn + mlogm)
# Space: O(n)

# sort, dp, two pointers

class Solution(object):
    def maxWalls(self, robots, distance, walls):
        """
        :type robots: List[int]
        :type distance: List[int]
        :type walls: List[int]
        :rtype: int
        """
        x_d = [(0, 0)]+sorted(zip(robots, distance), key=lambda x: x[0])+[(float("inf"), 0)]
        walls.sort()
        left0 = left1 = right = curr = 0
        dp, new_dp = [0]*2, [0]*2
        for i in xrange(1, len(x_d)-1):
            while curr < len(walls) and walls[curr] < x_d[i][0]:
                curr += 1
            r = min(x_d[i][0]+x_d[i][1], x_d[i+1][0]-1)
            while right < len(walls) and walls[right] <= r:
                right += 1
            new_dp[1] = max(dp[0], dp[1])+(right-curr)
            if curr < len(walls) and walls[curr] == x_d[i][0]:
                curr += 1
            l0 = max(x_d[i][0]-x_d[i][1], x_d[i-1][0]+1)
            while left0 < len(walls) and walls[left0] < l0:
                left0 += 1
            l1 = max(min(x_d[i-1][0]+x_d[i-1][1], x_d[i][0]-1)+1,
                     max(x_d[i][0]-x_d[i][1], x_d[i-1][0]+1))
            while left1 < len(walls) and walls[left1] < l1:
                left1 += 1
            new_dp[0] = max(dp[0]+(curr-left0), dp[1]+(curr-left1))
            dp, new_dp = new_dp, dp
        return max(dp[0], dp[1])