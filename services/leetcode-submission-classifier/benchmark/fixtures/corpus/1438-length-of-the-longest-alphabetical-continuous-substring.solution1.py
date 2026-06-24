# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: length-of-the-longest-alphabetical-continuous-substring
# source_path: LeetCode-Solutions-master/Python/length-of-the-longest-alphabetical-continuous-substring.py
# solution_class: Solution
# submission_id: 615f895e999d085b84a51114108848fe50a1da72
# seed: 1525222476

# Time:  O(n)
# Space: O(1)

# string

class Solution(object):
    def longestContinuousSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = l = 0
        for i in xrange(len(s)):
            l += 1
            if i+1 == len(s) or ord(s[i])+1 != ord(s[i+1]):
                result = max(result, l)
                l = 0
        return result