# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-time-to-remove-all-cars-containing-illegal-goods
# source_path: LeetCode-Solutions-master/Python/minimum-time-to-remove-all-cars-containing-illegal-goods.py
# solution_class: Solution
# submission_id: 29a3bce2eaf0c4902387bef1114e9071e9b9d025
# seed: 185559920

# Time:  O(n)
# Space: O(1)

# dp

class Solution(object):
    def minimumTime(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        result = left+(len(s)-0)
        for i in xrange(1, len(s)+1):
            left = min(left+2*(s[i-1] == '1'), i)
            result = min(result, left+(len(s)-i))
        return result