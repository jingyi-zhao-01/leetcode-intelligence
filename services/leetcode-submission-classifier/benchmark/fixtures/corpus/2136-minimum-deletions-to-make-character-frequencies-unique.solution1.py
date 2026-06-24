# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-deletions-to-make-character-frequencies-unique
# source_path: LeetCode-Solutions-master/Python/minimum-deletions-to-make-character-frequencies-unique.py
# solution_class: Solution
# submission_id: 9e9d4d917c7bb4bd2d341378fab7b9c10c9d9758
# seed: 2017590655

# Time:  O(n)
# Space: O(1)

import collections
import string

class Solution(object):
    def minDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = collections.Counter(s)
        result = 0
        lookup = set()
        for c in string.ascii_lowercase:
            for i in reversed(xrange(1, count[c]+1)):
                if i not in lookup:
                    lookup.add(i)
                    break
                result += 1
        return result