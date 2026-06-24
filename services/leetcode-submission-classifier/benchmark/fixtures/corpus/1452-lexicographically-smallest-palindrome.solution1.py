# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: lexicographically-smallest-palindrome
# source_path: LeetCode-Solutions-master/Python/lexicographically-smallest-palindrome.py
# solution_class: Solution
# submission_id: f435defaafcfe452f53b6a099304b45fffb41c83
# seed: 2096246793

# Time:  O(n)
# Space: O(1)

# greedy

class Solution(object):
    def makeSmallestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        return "".join(min(s[i], s[~i]) for i in xrange(len(s)))