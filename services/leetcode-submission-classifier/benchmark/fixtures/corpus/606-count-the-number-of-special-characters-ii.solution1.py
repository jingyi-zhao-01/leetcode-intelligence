# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-the-number-of-special-characters-ii
# source_path: LeetCode-Solutions-master/Python/count-the-number-of-special-characters-ii.py
# solution_class: Solution
# submission_id: d32c0156e720d1b7b2df02b26a230d56715e85f0
# seed: 3039410535

# Time:  O(n + 26)
# Space: O(26)

import itertools


# hash table

class Solution(object):
    def numberOfSpecialChars(self, word):
        """
        :type word: str
        :rtype: int
        """
        lookup1 = [len(word)]*26
        lookup2 = [-1]*26
        for i, x in enumerate(word):
            if x.islower():
                lookup1[ord(x)-ord('a')] = i
            elif lookup2[ord(x)-ord('A')] == -1:
                lookup2[ord(x)-ord('A')] = i
        return sum(x < y for x, y in itertools.izip(lookup1, lookup2))