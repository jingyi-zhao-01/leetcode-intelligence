# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-the-longest-semi-repetitive-substring
# source_path: LeetCode-Solutions-master/Python/find-the-longest-semi-repetitive-substring.py
# solution_class: Solution
# submission_id: a7a7747dbace118a34e13e22b9a1996116dd7110
# seed: 3518844588

# Time:  O(n)
# Space: O(1)

# two pointers

class Solution(object):
    def longestSemiRepetitiveSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = left = prev = 0
        for right in xrange(len(s)):
            if right-1 >= 0 and s[right-1] == s[right]:
                left, prev = prev, right
            result = max(result, right-left+1)
        return result