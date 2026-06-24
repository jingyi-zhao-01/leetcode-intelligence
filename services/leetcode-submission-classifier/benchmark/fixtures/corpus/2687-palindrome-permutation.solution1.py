# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: palindrome-permutation
# source_path: LeetCode-Solutions-master/Python/palindrome-permutation.py
# solution_class: Solution
# submission_id: 97cd8b6123ead7f543c812182c37fca0bc173a7a
# seed: 1949798210

# Time:  O(n)
# Space: O(1)

import collections

class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return sum(v % 2 for v in collections.Counter(s).values()) < 2