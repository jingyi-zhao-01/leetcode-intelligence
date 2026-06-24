# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: shortest-subarray-to-be-removed-to-make-array-sorted
# source_path: LeetCode-Solutions-master/Python/shortest-subarray-to-be-removed-to-make-array-sorted.py
# solution_class: Solution2
# submission_id: bdd48cdc46c278cfd3ffc7ab0d96cd1703ca40b6
# seed: 1306015744

# Time:  O(n)
# Space: O(1)

class Solution2(object):
    def findLengthOfShortestSubarray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        result = 0
        for i in xrange(1, len(arr)):
            if arr[i-1] <= arr[i]:
                continue
            j = len(arr)-1
            while j > i and (j == len(arr)-1 or arr[j] <= arr[j+1]) and arr[i-1] <= arr[j]:
                j -= 1
            result = j-i+1
            break
        for j in reversed(xrange(len(arr)-1)):
            if arr[j] <= arr[j+1]:
                continue
            i = 0
            while i < j and (i == 0 or arr[i-1] <= arr[i]) and arr[i] <= arr[j+1]:
                i += 1
            result = min(result, j-i+1)
            break
        return result