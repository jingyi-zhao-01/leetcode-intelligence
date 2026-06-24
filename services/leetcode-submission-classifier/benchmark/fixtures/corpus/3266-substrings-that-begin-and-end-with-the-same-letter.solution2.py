# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: substrings-that-begin-and-end-with-the-same-letter
# source_path: LeetCode-Solutions-master/Python/substrings-that-begin-and-end-with-the-same-letter.py
# solution_class: Solution
# submission_id: 319f09188adfc68c7d92fb372e51ea4eb838199c
# seed: 33269361

# Time:  O(n)
# Space: O(1)

import collections

class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        return sum(v*(v+1)//2 for v in collections.Counter(s).itervalues())