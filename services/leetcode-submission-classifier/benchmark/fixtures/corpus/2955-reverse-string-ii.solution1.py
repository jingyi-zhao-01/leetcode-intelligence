# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: reverse-string-ii
# source_path: LeetCode-Solutions-master/Python/reverse-string-ii.py
# solution_class: Solution
# submission_id: 20a73097e73303cc2ad405c2a31bcd2fda81fbc0
# seed: 1626260767

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s = list(s)
        for i in xrange(0, len(s), 2*k):
            s[i:i+k] = reversed(s[i:i+k])
        return "".join(s)