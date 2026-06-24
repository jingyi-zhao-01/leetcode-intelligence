# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-time-to-break-locks-i
# source_path: LeetCode-Solutions-master/Python/minimum-time-to-break-locks-i.py
# solution_class: Solution2
# submission_id: 29acfdb846773b43d2e903432fab059313e36f06
# seed: 3047371534

# Time:  O(n^3)
# Space: O(n^2)

# hungarian algorithm, weighted bipartite matching

class Solution2(object):
    def findMinimumTime(self, strength, K):
        """
        :type strength: List[int]
        :type K: int
        :rtype: int
        """
        def ceil_divide(a, b):
            return (a+b-1)//b
    
        def popcount(x):
            return bin(x).count('1')
    
        dp = [float('inf')]*(1<<len(strength))
        dp[0] = 0
        for mask in xrange(1, len(dp)):
            x = 1+(popcount(mask)-1)*K
            for i in xrange(len(strength)):
                if not (mask&(1<<i)):
                    continue
                dp[mask] = min(dp[mask], dp[mask^(1<<i)]+ceil_divide(strength[i], x))
        return dp[-1]