# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-good-binary-strings
# source_path: LeetCode-Solutions-master/Python/number-of-good-binary-strings.py
# solution_class: Solution
# submission_id: cae66adc444cc628473203df21647adc4c79c067
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
        for i in xrange(maxLength+1):
            dp[i%w] = 1 if i == 0 else 0
            if i-oneGroup >= 0:
                dp[i%w] = (dp[i%w]+dp[(i-oneGroup)%w])%MOD
            if i-zeroGroup >= 0:
                dp[i%w] = (dp[i%w]+dp[(i-zeroGroup)%w])%MOD
            if i >= minLength:
                result = (result+dp[i%w])%MOD
        return result