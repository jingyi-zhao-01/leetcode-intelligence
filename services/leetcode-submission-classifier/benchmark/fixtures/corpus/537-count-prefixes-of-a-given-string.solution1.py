# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-prefixes-of-a-given-string
# source_path: LeetCode-Solutions-master/Python/count-prefixes-of-a-given-string.py
# solution_class: Solution
# submission_id: 178d922cbce45c24fc3dbd52b53212814d309cb0
# seed: 924582916

# Time:  O(n * l)
# Space: O(1)

import itertools


# string

class Solution(object):
    def countPrefixes(self, words, s):
        """
        :type words: List[str]
        :type s: str
        :rtype: int
        """
        return sum(itertools.imap(s.startswith, words))