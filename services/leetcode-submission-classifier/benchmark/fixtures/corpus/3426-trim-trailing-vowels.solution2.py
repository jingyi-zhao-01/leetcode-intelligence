# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: trim-trailing-vowels
# source_path: LeetCode-Solutions-master/Python/trim-trailing-vowels.py
# solution_class: Solution2
# submission_id: 3146542f46702d6431781ea0f6b6c71d3257b347
# seed: 1557007612

# Time:  O(n)
# Space: O(1)

# string

class Solution2(object):
    def trimTrailingVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        VOWELS = "aeiou"
        i = next((i for i in reversed(xrange(len(s))) if s[i] not in VOWELS), -1)
        return s[:i+1]