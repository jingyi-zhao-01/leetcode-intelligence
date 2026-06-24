# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: kth-missing-positive-number
# source_path: LeetCode-Solutions-master/Python/kth-missing-positive-number.py
# solution_class: Solution
# submission_id: 27c9efc6d8108d68d5a986ba64b7ef0963e6bbde
# seed: 2400734442

# Time:  O(logn)
# Space: O(1)

class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        def check(arr, k, x):
            return arr[x]-(x+1) < k

        left, right = 0, len(arr)-1
        while left <= right:
            mid = left + (right-left)//2
            if not check(arr, k, mid):
                right = mid-1
            else:
                left = mid+1
        return right+1+k  # arr[right] + (k-(arr[right]-(right+1))) if right >= 0 else k