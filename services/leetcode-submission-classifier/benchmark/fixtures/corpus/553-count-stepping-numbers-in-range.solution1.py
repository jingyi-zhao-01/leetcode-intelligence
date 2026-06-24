# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-stepping-numbers-in-range
# source_path: LeetCode-Solutions-master/Python/count-stepping-numbers-in-range.py
# solution_class: Solution
# submission_id: 4e17dfaa9dac983231187bb90bf31a6a4695a817
# seed: 3883682094

# Time:  O(n)
# Space: O(1)

# dp

class Solution(object):
    def countSteppingNumbers(self, low, high):
        """
        :type low: str
        :type high: str
        :rtype: int
        """
        MOD = 10**9+7
        def f(s):
            dp = [[0]*10 for _ in xrange(2)]
            for j in xrange(1, ord(s[0])-ord('0')+1):
                dp[0][j] = 1
            prefix = True
            for i in xrange(1, len(s)):
                for j in xrange(10):
                    dp[i%2][j] = int(j != 0)
                    if j-1 >= 0:
                        dp[i%2][j] = (dp[i%2][j]+(dp[(i-1)%2][j-1]-int(prefix and (ord(s[i-1])-ord('0')) == j-1 and j > (ord(s[i])-ord('0')))))%MOD
                    if j+1 < 10:
                        dp[i%2][j] = (dp[i%2][j]+(dp[(i-1)%2][j+1]-int(prefix and (ord(s[i-1])-ord('0')) == j+1 and j > (ord(s[i])-ord('0')))))%MOD
                if abs(ord(s[i])-ord(s[i-1])) != 1:
                    prefix = False
            return reduce(lambda x, y: (x+y)%MOD, dp[(len(s)-1)%2])

        return (f(high)-f(str(int(low)-1)))%MOD