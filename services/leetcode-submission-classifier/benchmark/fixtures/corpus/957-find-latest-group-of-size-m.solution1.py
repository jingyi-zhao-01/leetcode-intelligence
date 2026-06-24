# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-latest-group-of-size-m
# source_path: LeetCode-Solutions-master/Python/find-latest-group-of-size-m.py
# solution_class: Solution
# submission_id: d3e121530116bcb0917ec020a03b7a3d91cc4cb9
# seed: 1517313906

# Time:  O(n)
# Space: O(n)

class Solution(object):
    def findLatestStep(self, arr, m):
        """
        :type arr: List[int]
        :type m: int
        :rtype: int
        """
        if m == len(arr):
            return m
        length = [0]*(len(arr)+2)
        result = -1
        for i, x in enumerate(arr):
            left, right = length[x-1], length[x+1]
            if left == m or right == m:
                result = i
            length[x-left] = length[x+right] = left+right+1
        return result