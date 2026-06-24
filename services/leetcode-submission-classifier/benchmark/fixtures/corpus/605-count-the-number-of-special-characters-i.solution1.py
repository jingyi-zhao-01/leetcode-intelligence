# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-the-number-of-special-characters-i
# source_path: LeetCode-Solutions-master/Python/count-the-number-of-special-characters-i.py
# solution_class: Solution
# submission_id: 39fc1025c0fb155a1f26bafb316b9c547a789c87
# seed: 3310518738

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
        lookup1 = [False]*26
        lookup2 = [False]*26
        for x in word:
            if x.islower():
                lookup1[ord(x)-ord('a')] = True
            else:
                lookup2[ord(x)-ord('A')] = True
        return sum(x == y == True for x, y in itertools.izip(lookup1, lookup2))