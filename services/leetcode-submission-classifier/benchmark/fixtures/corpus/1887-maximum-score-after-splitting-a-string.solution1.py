# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-score-after-splitting-a-string
# source_path: LeetCode-Solutions-master/Python/maximum-score-after-splitting-a-string.py
# solution_class: Solution
# submission_id: be695fbbd8dd24e253e325c2aee6be276240f84c
# seed: 3862682500

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        result, zeros, ones = 0, 0, 0
        for i in xrange(1, len(s)-1):
            if s[i] == '0':
                zeros += 1
            else:
                ones += 1
            result = max(result, zeros-ones)
        return result + ones + (s[0] == '0') + (s[-1] == '1')