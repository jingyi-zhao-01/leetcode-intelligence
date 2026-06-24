# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-first-palindromic-string-in-the-array
# source_path: LeetCode-Solutions-master/Python/find-first-palindromic-string-in-the-array.py
# solution_class: Solution
# submission_id: 182347f638443f73d3d606a214b36bde20ad8bd1
# seed: 1916179211

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def firstPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        def is_palindrome(s):
            i, j = 0, len(s)-1
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        for w in words:
            if is_palindrome(w):
                return w
        return ""