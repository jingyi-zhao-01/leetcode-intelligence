# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-substrings-without-repeating-character
# source_path: LeetCode-Solutions-master/Python/count-substrings-without-repeating-character.py
# solution_class: Solution
# submission_id: 9e3cee9ddabee705d0fb11362e7c65b39b58c757
# seed: 2023345319

# Time:  O(n)
# Space: O(1)

# two pointers, sliding window

class Solution(object):
    def numberOfSpecialSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = left = 0
        lookup = [-1]*26
        for right in xrange(len(s)):
            if lookup[ord(s[right])-ord('a')] >= left:
                left = lookup[ord(s[right])-ord('a')]+1
            lookup[ord(s[right])-ord('a')] = right
            result += (right-left+1)
        return result