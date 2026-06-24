# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: remove-palindromic-subsequences
# source_path: LeetCode-Solutions-master/Python/remove-palindromic-subsequences.py
# solution_class: Solution
# submission_id: 37861f1b6325f6da0dc206e7b5a95dde02f19743
# seed: 2308516109

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def removePalindromeSub(self, s):
        """
        :type s: str
        :rtype: int
        """
        def is_palindrome(s):
            for i in xrange(len(s)//2):
                if s[i] != s[-1-i]:
                    return False
            return True
        
        return 2 - is_palindrome(s) - (s == "")