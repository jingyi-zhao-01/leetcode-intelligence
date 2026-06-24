# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: compare-version-numbers
# source_path: LeetCode-Solutions-master/Python/compare-version-numbers.py
# solution_class: Solution
# submission_id: e3c5387f6a73c1280b7b0f89f0b1ad4eed35f4d8
# seed: 2465852720

# Time:  O(n)
# Space: O(1)

import itertools

class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        n1, n2 = len(version1), len(version2)
        i, j = 0, 0
        while i < n1 or j < n2:
            v1, v2 = 0, 0
            while i < n1 and version1[i] != '.':
                v1 = v1 * 10 + int(version1[i])
                i += 1
            while j < n2 and version2[j] != '.':
                v2 = v2 * 10 + int(version2[j])
                j += 1
            if v1 != v2:
                return 1 if v1 > v2 else -1
            i += 1
            j += 1

        return 0