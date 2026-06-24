# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: vowel-consonant-score
# source_path: LeetCode-Solutions-master/Python/vowel-consonant-score.py
# solution_class: Solution
# submission_id: 39b0e3775f0e7274c45ccca14440dbbe8c196574
# seed: 3139756284

# Time:  O(n)
# Space: O(1)

# string

class Solution(object):
    def vowelConsonantScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        VOWELS = "aeiou"
        v = c = 0
        for x in s:
            if x in VOWELS:
                v += 1
            elif x.isalpha():
                c += 1
        return v//c if c else 0