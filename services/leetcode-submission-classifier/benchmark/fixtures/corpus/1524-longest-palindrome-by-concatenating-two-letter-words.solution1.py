# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: longest-palindrome-by-concatenating-two-letter-words
# source_path: LeetCode-Solutions-master/Python/longest-palindrome-by-concatenating-two-letter-words.py
# solution_class: Solution
# submission_id: 7e04f70b1feba6692b272675971b081980db85ae
# seed: 282212158

# Time:  O(n)
# Space: O(n)

import collections

class Solution(object):
    def longestPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        cnt = collections.Counter(words)
        result = remain = 0
        for x, c in cnt.iteritems():
            if x == x[::-1]:
                result += c//2
                remain |= c%2
            elif x < x[::-1] and x[::-1] in cnt:
                result += min(c, cnt[x[::-1]])
        return result*4+remain*2