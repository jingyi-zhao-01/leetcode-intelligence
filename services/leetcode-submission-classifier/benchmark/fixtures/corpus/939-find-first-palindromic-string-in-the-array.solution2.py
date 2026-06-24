# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-first-palindromic-string-in-the-array
# source_path: LeetCode-Solutions-master/Python/find-first-palindromic-string-in-the-array.py
# solution_class: Solution2
# submission_id: 09262cdef0f1400a064ba12a37cafd9c336f1054
# seed: 2488535237

# Time:  O(n)
# Space: O(1)

class Solution2(object):
    def firstPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        return next((x for x in words if x == x[::-1]), "")