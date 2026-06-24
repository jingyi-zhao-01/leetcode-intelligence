# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: add-bold-tag-in-string
# source_path: LeetCode-Solutions-master/Python/add-bold-tag-in-string.py
# solution_class: Solution
# submission_id: 56f287332cdb107c366a06c055ec2b1c753d264b
# seed: 1681592325

# Time:  O(n * d * l), l is the average string length
# Space: O(n)

import collections
import functools


# 59ms

class Solution(object):
    def addBoldTag(self, s, dict):
        """
        :type s: str
        :type dict: List[str]
        :rtype: str
        """
        lookup = [0] * len(s)
        for d in dict:
            pos = s.find(d)
            while pos != -1:
                lookup[pos:pos+len(d)] = [1] * len(d)
                pos = s.find(d, pos + 1)

        result = []
        for i in xrange(len(s)):
            if lookup[i] and (i == 0 or not lookup[i-1]):
                result.append("<b>")
            result.append(s[i])
            if lookup[i] and (i == len(s)-1 or not lookup[i+1]):
                result.append("</b>")
        return "".join(result)