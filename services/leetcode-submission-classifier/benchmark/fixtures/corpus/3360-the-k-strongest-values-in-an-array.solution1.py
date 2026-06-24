# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: the-k-strongest-values-in-an-array
# source_path: LeetCode-Solutions-master/Python/the-k-strongest-values-in-an-array.py
# solution_class: Solution
# submission_id: a3fc3b678f3ab7a5ff07485182d22d85e49d70a9
# seed: 2079468220

# Time:  O(nlogn)
# Space: O(1)

class Solution(object):
    def getStrongest(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        arr.sort()
        m = arr[(len(arr)-1)//2]
        result = []
        left, right = 0, len(arr)-1
        while len(result) < k:
            if m-arr[left] > arr[right]-m:
                result.append(arr[left])
                left += 1
            else:
                result.append(arr[right])
                right -= 1
        return result