# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: element-appearing-more-than-25-in-sorted-array
# source_path: LeetCode-Solutions-master/Python/element-appearing-more-than-25-in-sorted-array.py
# solution_class: Solution
# submission_id: b73cabd0624db3d13fa93264889dcc401c36679d
# seed: 2869782146

# Time:  O(logn)
# Space: O(1)

import bisect

class Solution(object):
    def findSpecialInteger(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        for x in [arr[len(arr)//4], arr[len(arr)//2], arr[len(arr)*3//4]]:
            if (bisect.bisect_right(arr, x) - bisect.bisect_left(arr, x)) * 4 > len(arr):
                return x
        return -1