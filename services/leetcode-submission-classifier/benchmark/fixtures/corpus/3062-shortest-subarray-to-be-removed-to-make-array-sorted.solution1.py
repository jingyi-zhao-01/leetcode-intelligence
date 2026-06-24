# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: shortest-subarray-to-be-removed-to-make-array-sorted
# source_path: LeetCode-Solutions-master/Python/shortest-subarray-to-be-removed-to-make-array-sorted.py
# solution_class: Solution
# submission_id: a86c296f573ff31e2a92bb32ba8b0848aef7e76e
# seed: 2242016119

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def findLengthOfShortestSubarray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        j = -1
        for j in reversed(xrange(1, len(arr))):
            if arr[j-1] > arr[j]:
                break
        else:
            return 0
        result = j
        for i in xrange(j):
            if i and arr[i] < arr[i-1]:
                break
            while j < len(arr) and arr[i] > arr[j]:
                j += 1
            result = min(result, (j-i+1)-2)
        return result