# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: longest-palindrome
# source_path: LeetCode-Solutions-master/Python/longest-palindrome.py
# solution_class: Solution
# submission_id: 87ece74c27ba58029160a9915e271eb32d24f0a5
# seed: 3267521288

# Time:  O(n)
# Space: O(1)

import collections

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        odds = 0
        for k, v in collections.Counter(s).iteritems():
            odds += v & 1
        return len(s) - odds + int(odds > 0)

    def longestPalindrome2(self, s):
        """
        :type s: str
        :rtype: int
        """
        odd = sum(map(lambda x: x & 1, collections.Counter(s).values()))
        return len(s) - odd + int(odd > 0)