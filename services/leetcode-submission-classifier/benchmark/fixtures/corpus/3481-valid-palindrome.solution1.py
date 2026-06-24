# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: valid-palindrome
# source_path: LeetCode-Solutions-master/Python/valid-palindrome.py
# solution_class: Solution
# submission_id: 845548e75a5fee45472b07cb751ace6350d69701
# seed: 2383017803

# Time:  O(n)
# Space: O(1)

class Solution(object):
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        i, j = 0, len(s) - 1
        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1
            if s[i].lower() != s[j].lower():
                return False
            i, j = i + 1, j - 1
        return True