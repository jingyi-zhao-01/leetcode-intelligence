# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-substrings-without-repeating-character
# source_path: LeetCode-Solutions-master/Python/count-substrings-without-repeating-character.py
# solution_class: Solution2
# submission_id: 4fe58b5f539cfcaab6a869e3c46c383c80d3065f
# seed: 1216586135

# Time:  O(n)
# Space: O(1)

# two pointers, sliding window

class Solution2(object):
    def numberOfSpecialSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = left = 0
        lookup = [False]*26
        for right in xrange(len(s)):
            while lookup[ord(s[right])-ord('a')]:
                lookup[ord(s[left])-ord('a')] = False
                left += 1
            lookup[ord(s[right])-ord('a')] = True
            result += (right-left+1)
        return result