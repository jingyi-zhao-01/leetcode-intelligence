# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-pairs-of-equal-substrings-with-minimum-difference
# source_path: LeetCode-Solutions-master/Python/count-pairs-of-equal-substrings-with-minimum-difference.py
# solution_class: Solution
# submission_id: a61b8f1a537bc44d12ebc27e0269edc7de28b3a6
# seed: 3695724503

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def countQuadruples(self, firstString, secondString):
        """
        :type firstString: str
        :type secondString: str
        :rtype: int
        """
        lookup1 = [-1]*26
        for i in reversed(xrange(len(firstString))):
            lookup1[ord(firstString[i])-ord('a')] = i
        lookup2 = [-1]*26
        for i in xrange(len(secondString)):
            lookup2[ord(secondString[i])-ord('a')] = i
        result, diff = 0, float("inf")
        for i in xrange(26):
            if lookup1[i] == -1 or lookup2[i] == -1:
                continue
            if lookup1[i]-lookup2[i] < diff:
                diff = lookup1[i]-lookup2[i]
                result = 0
            result += int(lookup1[i]-lookup2[i] == diff)
        return result