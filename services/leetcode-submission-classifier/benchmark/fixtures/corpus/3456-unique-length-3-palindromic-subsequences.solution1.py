# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: unique-length-3-palindromic-subsequences
# source_path: LeetCode-Solutions-master/Python/unique-length-3-palindromic-subsequences.py
# solution_class: Solution
# submission_id: 2ab0a705e7348169ad9211714db90312bbc76e37
# seed: 50350482

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def countPalindromicSubsequence(self, s):
        """
        :type s: str
        :rtype: int
        """
        first, last = [len(s)]*26, [-1]*26
        for i, c in enumerate(s):
            first[ord(c)-ord('a')] = min(first[ord(c)-ord('a')], i)
            last[ord(c)-ord('a')] = max(last[ord(c)-ord('a')], i)
        return sum(len(set(s[i] for i in xrange(first[c]+1, last[c]))) for c in xrange(26))