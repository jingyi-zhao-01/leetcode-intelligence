# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-substrings-containing-all-three-characters
# source_path: LeetCode-Solutions-master/Python/number-of-substrings-containing-all-three-characters.py
# solution_class: Solution
# submission_id: 2c2fe022898cb3b98366f2773217ae47c7e440b7
# seed: 43682769

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        result, left = 0, [-1]*3
        for right, c in enumerate(s):
            left[ord(c)-ord('a')] = right
            result += min(left)+1
        return result