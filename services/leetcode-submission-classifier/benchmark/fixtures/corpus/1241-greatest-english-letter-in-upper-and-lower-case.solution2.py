# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: greatest-english-letter-in-upper-and-lower-case
# source_path: LeetCode-Solutions-master/Python/greatest-english-letter-in-upper-and-lower-case.py
# solution_class: Solution2
# submission_id: 0214ed1be034b61663b6bba5827a28bd84cbc3ed
# seed: 1804265802

# Time:  O(n)
# Space: O(1)

# string, hash table

class Solution2(object):
    def greatestLetter(self, s):
        """
        :type s: str
        :rtype: str
        """
        lookup = set(s)
        return next((C for c, C in itertools.izip(reversed(string.ascii_lowercase), reversed(string.ascii_uppercase)) if c in lookup and C in lookup), "")