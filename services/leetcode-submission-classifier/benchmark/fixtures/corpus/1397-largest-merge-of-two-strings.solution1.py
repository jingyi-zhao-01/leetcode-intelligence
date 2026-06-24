# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: largest-merge-of-two-strings
# source_path: LeetCode-Solutions-master/Python/largest-merge-of-two-strings.py
# solution_class: Solution
# submission_id: a04dafb8427a261e33fc265712a2abc02dde75f1
# seed: 931502002

# Time:  O(n * m)
# Space: O(n + m)

import collections

class Solution(object):
    def largestMerge(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        q1 = collections.deque(word1)
        q2 = collections.deque(word2)
        result = []
        while q1 or q2:
            if q1 > q2:
                result.append(q1.popleft())
            else:
                result.append(q2.popleft())
        return "".join(result)