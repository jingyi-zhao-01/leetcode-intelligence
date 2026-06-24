# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: shortest-distance-to-target-color
# source_path: LeetCode-Solutions-master/Python/shortest-distance-to-target-color.py
# solution_class: Solution
# submission_id: cab442ca7ec6383e4720cdad4c357def1e2c51a0
# seed: 130060554

# Time:  O(n)
# Space: O(n)

class Solution(object):
    def shortestDistanceColor(self, colors, queries):
        """
        :type colors: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        dp = [[-1 for _ in xrange(len(colors))] for _ in xrange(3)]
        dp[colors[0]-1][0] = 0
        for i in xrange(1, len(colors)):
            for color in xrange(3):
                dp[color][i] = dp[color][i-1]
            dp[colors[i]-1][i] = i

        dp[colors[len(colors)-1]-1][len(colors)-1] = len(colors)-1
        for i in reversed(xrange(len(colors)-1)):
            for color in xrange(3):
                if dp[color][i+1] == -1:
                    continue
                if dp[color][i] == -1 or \
                   abs(dp[color][i+1]-i) < abs(dp[color][i]-i):
                    dp[color][i] = dp[color][i+1]
            dp[colors[i]-1][i] = i
         
        return [abs(dp[color-1][i]-i) if dp[color-1][i] != -1 else -1 \
                    for i, color in queries]