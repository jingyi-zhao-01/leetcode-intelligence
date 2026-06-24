# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: expressive-words
# source_path: LeetCode-Solutions-master/Python/expressive-words.py
# solution_class: Solution
# submission_id: ee2c5c06863dac663633c5945eb95fdd838c9318
# seed: 726227033

# Time:  O(n + s), n is the sum of all word lengths, s is the length of S
# Space: O(l + s), l is the max word length

import itertools

class Solution(object):
    def expressiveWords(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        # Run length encoding
        def RLE(S):
            return itertools.izip(*[(k, len(list(grp)))
                                  for k, grp in itertools.groupby(S)])

        R, count = RLE(S)
        result = 0
        for word in words:
            R2, count2 = RLE(word)
            if R2 != R:
                continue
            result += all(c1 >= max(c2, 3) or c1 == c2
                          for c1, c2 in itertools.izip(count, count2))
        return result