# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: make-three-strings-equal
# source_path: LeetCode-Solutions-master/Python/make-three-strings-equal.py
# solution_class: Solution
# submission_id: d947971dc8cb51dcedcc0466916f7a22182a9480
# seed: 1727153030

# Time:  O(n)
# Space: O(1)

import itertools


# string

class Solution(object):
    def findMinimumOperations(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: int
        """
        for i, (a, b, c) in enumerate(itertools.izip(s1, s2, s3)):
            if not a == b == c:
                break
        else:
            i += 1
        return len(s1)+len(s2)+len(s3)-3*i if i else -1