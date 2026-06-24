# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-height-by-stacking-cuboids
# source_path: LeetCode-Solutions-master/Python/maximum-height-by-stacking-cuboids.py
# solution_class: Solution
# submission_id: 06ca010e546111571c1ee528ccc270f4c5cf69d5
# seed: 4196345646

# Time:  O(n^2)
# Space: O(n)
    

class Solution(object):
    def maxHeight(self, cuboids):
        """
        :type cuboids: List[List[int]]
        :rtype: int
        """
        for cuboid in cuboids:
            cuboid.sort()
        cuboids.append([0, 0, 0])
        cuboids.sort()
        dp = [0]*len(cuboids)
        for i in xrange(1, len(cuboids)):
            for j in xrange(i):
                if all(cuboids[j][k] <= cuboids[i][k] for k in xrange(3)):
                    dp[i] = max(dp[i], dp[j]+cuboids[i][2])
        return max(dp)