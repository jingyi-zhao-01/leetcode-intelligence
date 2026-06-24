# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-k-closest-elements
# source_path: LeetCode-Solutions-master/Python/find-k-closest-elements.py
# solution_class: Solution
# submission_id: 35b026f9f50dde2af9d60265fd6180468c2cf892
# seed: 2254243268

# Time:  O(logn + k)
# Space: O(1)

import bisect

class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        i = bisect.bisect_left(arr, x)
        left, right = i-1, i
        while k:
            if right >= len(arr) or \
               (left >= 0 and abs(arr[left]-x) <= abs(arr[right]-x)):
                left -= 1
            else:
                right += 1
            k -= 1
        return arr[left+1:right]