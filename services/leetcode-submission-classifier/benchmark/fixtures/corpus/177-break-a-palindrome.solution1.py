# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: break-a-palindrome
# source_path: LeetCode-Solutions-master/Python/break-a-palindrome.py
# solution_class: Solution
# submission_id: b1f571e5faca1a3d5a04be4bc7b9c4cee6c5c5b2
# seed: 4006167979

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def breakPalindrome(self, palindrome):
        """
        :type palindrome: str
        :rtype: str
        """
        for i in xrange(len(palindrome)//2):
            if palindrome[i] != 'a':
                return palindrome[:i] + 'a' + palindrome[i+1:]
        return palindrome[:-1] + 'b' if len(palindrome) >= 2 else ""