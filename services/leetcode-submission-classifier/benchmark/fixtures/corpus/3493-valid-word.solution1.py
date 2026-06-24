# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: valid-word
# source_path: LeetCode-Solutions-master/Python/valid-word.py
# solution_class: Solution
# submission_id: 679beddb8efd67d86b7ae81c3fe2883a3157f90f
# seed: 2357353462

# Time:  O(n)
# Space: O(1)

# string

class Solution(object):
    def isValid(self, word):
        """
        :type word: str
        :rtype: bool
        """
        VOWELS = "aeiou"

        if len(word) < 3:
            return False
        vowel = consonant = False
        for x in word:
            if x.isalpha():
                if x.lower() in VOWELS:
                    vowel = True
                else:
                    consonant = True
            elif not x.isdigit():
                return False
        return vowel and consonant