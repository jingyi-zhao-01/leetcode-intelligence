# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-balanced-integers-in-a-range
# source_path: LeetCode-Solutions-master/Python/number-of-balanced-integers-in-a-range.py
# solution_class: Solution
# submission_id: d81fa023bcbe7c2a5ca8581602a2659765bc5d0b
# seed: 2936983015

# Time:  O((logn)^2)
# Space: O(logn)

# dp

class Solution(object):
    def countBalanced(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: int
        """
        def count(n):
            digits = []
            while n:
                n, r = divmod(n, 10)
                digits.append(r)
            digits.reverse()
            dp = [[0]*2 for _ in xrange(len(digits)*9+1)]
            dp[0][1] = 1
            for i in xrange(len(digits)):
                new_dp = [[0]*2 for _ in xrange(len(digits)*9+1)]
                for curr in xrange(len(dp)):
                    curr -= len(digits)//2*9
                    for tight in xrange(2):
                        if not dp[curr][tight]:
                            continue
                        bound = digits[i] if tight else 9
                        for d in xrange(bound+1):
                            new_dp[curr-d if i&1 else curr+d][tight and d == bound] += dp[curr][tight]
                dp = new_dp
            return dp[0][0]
        
        return count(high+1)-count(low)