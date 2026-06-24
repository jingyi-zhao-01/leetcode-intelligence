# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: missing-number-in-arithmetic-progression
# source_path: LeetCode-Solutions-master/Python/missing-number-in-arithmetic-progression.py
# solution_class: Solution
# submission_id: c9430c808f6f6d02ecca13f1279b8719da144180
# seed: 2016175008

# Time:  O(logn)
# Space: O(1)

class Solution(object):
    def missingNumber(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        def check(arr, d, x):
            return arr[x] != arr[0] + d*x

        d = (arr[-1]-arr[0])//len(arr)
        left, right = 0, len(arr)-1
        while left <= right:
            mid = left + (right-left)//2
            if check(arr, d, mid):
                right = mid-1
            else:
                left = mid+1
        return arr[0] + d*left