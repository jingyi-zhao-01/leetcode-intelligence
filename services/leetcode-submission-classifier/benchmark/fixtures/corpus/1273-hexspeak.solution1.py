# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: hexspeak
# source_path: LeetCode-Solutions-master/Python/hexspeak.py
# solution_class: Solution
# submission_id: a6677a441ebdb2db0eb140f67930694695c0ef42
# seed: 864853574

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def toHexspeak(self, num):
        """
        :type num: str
        :rtype: str
        """
        lookup = {0:'O', 1:'I'}
        for i in xrange(6):
            lookup[10+i] = chr(ord('A')+i)
        result = []
        n = int(num)
        while n:
            n, r = divmod(n, 16)
            if r not in lookup:
                return "ERROR"
            result.append(lookup[r])
        return "".join(reversed(result))