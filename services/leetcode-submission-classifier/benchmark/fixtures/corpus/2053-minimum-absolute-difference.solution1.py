# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-absolute-difference
# source_path: LeetCode-Solutions-master/Python/minimum-absolute-difference.py
# solution_class: Solution
# submission_id: a305239880baba250a90657bb6364f3cd8bf6fa3
# seed: 449905058

# Time:  O(nlogn)
# Space: O(n)

class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        result = []
        min_diff = float("inf")
        arr.sort()
        for i in xrange(len(arr)-1):
            diff = arr[i+1]-arr[i]
            if diff < min_diff:
                min_diff = diff
                result = [[arr[i], arr[i+1]]]
            elif diff == min_diff:
                result.append([arr[i], arr[i+1]])
        return result