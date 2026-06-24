# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-substrings-starting-and-ending-with-given-character
# source_path: LeetCode-Solutions-master/Python/count-substrings-starting-and-ending-with-given-character.py
# solution_class: Solution
# submission_id: 8e530288f69ee6970345a4255b4c14d1798fa9c1
# seed: 1703354827

# Time:  O(n)
# Space: O(1)

# combinatorics

class Solution(object):
    def countSubstrings(self, s, c):
        """
        :type s: str
        :type c: str
        :rtype: int
        """
        n = s.count(c)
        return (n+1)*n//2