# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-time-to-remove-all-cars-containing-illegal-goods
# source_path: LeetCode-Solutions-master/Python/minimum-time-to-remove-all-cars-containing-illegal-goods.py
# solution_class: Solution2
# submission_id: 1e57f1a392f6ceecb84a06340a4cdf6d10729f59
# seed: 2109182454

# Time:  O(n)
# Space: O(1)

# dp

class Solution2(object):
    def minimumTime(self, s):
        """
        :type s: str
        :rtype: int
        """
        result, right = len(s), [0]*(len(s)+1)
        for i in reversed(xrange(len(s))):
            right[i] = min(right[i+1]+2*(s[i] == '1'), len(s)-i)
        left = 0
        result = left+right[0]
        for i in xrange(1, len(s)+1):
            left = min(left+2*(s[i-1] == '1'), i)     
            result = min(result, left+right[i])
        return result