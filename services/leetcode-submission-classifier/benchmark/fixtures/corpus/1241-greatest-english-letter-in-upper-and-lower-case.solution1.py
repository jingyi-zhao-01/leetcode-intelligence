# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: greatest-english-letter-in-upper-and-lower-case
# source_path: LeetCode-Solutions-master/Python/greatest-english-letter-in-upper-and-lower-case.py
# solution_class: Solution
# submission_id: a37ab0425f1d41bdcbcf86ef53f5ed4177f3049d
# seed: 1098579590

# Time:  O(n)
# Space: O(1)

# string, hash table

class Solution(object):
    def greatestLetter(self, s):
        """
        :type s: str
        :rtype: str
        """
        lookup = set(s)
        result = ""
        for c in s:
            if c.isupper() and lower(c) in s:
                if c > result:
                    result = c
        return result