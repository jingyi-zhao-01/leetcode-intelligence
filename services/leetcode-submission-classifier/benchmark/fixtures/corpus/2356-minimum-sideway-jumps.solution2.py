# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-sideway-jumps
# source_path: LeetCode-Solutions-master/Python/minimum-sideway-jumps.py
# solution_class: Solution2
# submission_id: e27c11b53909d611384d482c49cf8256e6eda0b4
# seed: 1565709202

# Time:  O(n)
# Space: O(1)

# greedy solution

class Solution2(object):
    def minSideJumps(self, obstacles):
        """
        :type obstacles: List[int]
        :rtype: int
        """
        dp = [1, 0, 1]        
        for i in obstacles:
            if i:
                dp[i-1] = float("inf")
            for j in xrange(3):
                if j+1 != i:
                    dp[j] = min(dp[0]+(j != 0), dp[1]+(j != 1), dp[2]+(j != 2))
        return min(dp)