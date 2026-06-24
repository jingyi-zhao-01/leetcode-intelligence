# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: valid-palindrome-ii
# source_path: LeetCode-Solutions-master/Python/valid-palindrome-ii.py
# solution_class: Solution
# submission_id: 6a2306bbd38299def4faed07ee72a985cb9e8219
# seed: 3872540701

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def validPalindrome(s, left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left, right = left+1, right-1
            return True

        left, right = 0, len(s)-1
        while left < right:
            if s[left] != s[right]:
                return validPalindrome(s, left, right-1) or validPalindrome(s, left+1, right)
            left, right = left+1, right-1
        return True