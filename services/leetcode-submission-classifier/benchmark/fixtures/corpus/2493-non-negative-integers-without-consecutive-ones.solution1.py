# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: non-negative-integers-without-consecutive-ones
# source_path: LeetCode-Solutions-master/Python/non-negative-integers-without-consecutive-ones.py
# solution_class: Solution
# submission_id: aaf24b030b1455d8d49e1583df8174a23ce4c9f9
# seed: 2800788462

# Time:  O(1)
# Space: O(1)

class Solution(object):
    def findIntegers(self, num):
        """
        :type num: int
        :rtype: int
        """
        dp = [0] * 32
        dp[0], dp[1] = 1, 2
        for i in xrange(2, len(dp)):
            dp[i] = dp[i-1] + dp[i-2]
        result, prev_bit = 0, 0
        for i in reversed(xrange(31)):
            if (num & (1 << i)) != 0:
                result += dp[i]
                if prev_bit == 1:
                    result -= 1
                    break
                prev_bit = 1
            else:
                prev_bit = 0
        return result + 1