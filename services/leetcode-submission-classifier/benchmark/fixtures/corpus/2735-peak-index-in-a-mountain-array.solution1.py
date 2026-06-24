# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: peak-index-in-a-mountain-array
# source_path: LeetCode-Solutions-master/Python/peak-index-in-a-mountain-array.py
# solution_class: Solution
# submission_id: cfa6d2b3e4508077887f110f4d33ead8b022e403
# seed: 4288584915

# Time:  O(logn)
# Space: O(1)

class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        left, right = 0, len(arr)-1
        while left <= right:
            mid = left + (right-left)//2
            if arr[mid] > arr[mid+1]:
                right = mid-1
            else:
                left = mid+1
        return left