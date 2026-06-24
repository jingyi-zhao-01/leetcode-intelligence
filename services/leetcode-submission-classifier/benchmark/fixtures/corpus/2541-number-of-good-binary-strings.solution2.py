# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-good-binary-strings
# source_path: LeetCode-Solutions-master/Python/number-of-good-binary-strings.py
# solution_class: Solution
# submission_id: a63b066a4a5c44336ba2c84bd96a2e706db6ff62
# seed: 2155737829

# Time:  O(n), n = maxLength
# Space: O(w), w = max(oneGroup, zeroGroup)+1

# dp

class Solution(object):
    def goodBinaryStrings(self, minLength, maxLength, oneGroup, zeroGroup):
        """
        :type minLength: int
        :type maxLength: int
        :type oneGroup: int
        :type zeroGroup: int
        :rtype: int
        """
        MOD = 10**9+7
        result = 0
        w = max(oneGroup, zeroGroup)+1
        dp = [0]*w
        dp[0] = 1
        for i in xrange(maxLength+1):
            if i >= minLength:
                result = (result+dp[i%w])%MOD
            if i+oneGroup <= maxLength:
                dp[(i+oneGroup)%w] = (dp[(i+oneGroup)%w]+dp[i%w])%MOD
            if i+zeroGroup <= maxLength:
                dp[(i+zeroGroup)%w] = (dp[(i+zeroGroup)%w]+dp[i%w])%MOD
            dp[i%w] = 0
        return result