# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-the-distance-value-between-two-arrays
# source_path: LeetCode-Solutions-master/Python/find-the-distance-value-between-two-arrays.py
# solution_class: Solution
# submission_id: f73473414e87f590983afab82a30e809fc64759d
# seed: 3122206808

# Time:  O((n + m) * logm)
# Space: O(1)

import bisect

class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type d: int
        :rtype: int
        """
        arr2.sort()
        result, i, j = 0, 0, 0
        for x in arr1:
            j = bisect.bisect_left(arr2, x)
            left = arr2[j-1] if j-1 >= 0 else float("-inf")
            right = arr2[j] if j < len(arr2) else float("inf")
            result += left+d < x < right-d
        return result