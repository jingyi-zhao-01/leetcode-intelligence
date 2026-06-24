# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: valid-palindrome-iv
# source_path: LeetCode-Solutions-master/Python/valid-palindrome-iv.py
# solution_class: Solution
# submission_id: 7346b9477b7f37e2b355483fa2dc9e9b5460e9ee
# seed: 355020234

# Time:  O(n)
# Space: O(1)

# string, two pointers

class Solution(object):
    def makePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return sum(s[i] != s[~i] for i in xrange(len(s)//2)) <= 2