# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-the-distance-value-between-two-arrays
# source_path: LeetCode-Solutions-master/Python/find-the-distance-value-between-two-arrays.py
# solution_class: Solution2
# submission_id: 3cc18cd809936fb4eee06c080f6af5a3e242e5bb
# seed: 284373599

# Time:  O((n + m) * logm)
# Space: O(1)

import bisect

class Solution2(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type d: int
        :rtype: int
        """
        arr1.sort(), arr2.sort()
        result, i, j = 0, 0, 0
        while i < len(arr1) and j < len(arr2):
            if arr1[i]-arr2[j] > d:
                j += 1
                continue
            result += arr2[j]-arr1[i] > d
            i += 1
        return result+len(arr1)-i