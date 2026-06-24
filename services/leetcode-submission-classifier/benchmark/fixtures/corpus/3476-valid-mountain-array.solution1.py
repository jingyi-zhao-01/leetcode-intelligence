# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: valid-mountain-array
# source_path: LeetCode-Solutions-master/Python/valid-mountain-array.py
# solution_class: Solution
# submission_id: f7741ed13f8b3dedbd013d3c4ae5dbc151452b69
# seed: 615888582

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        i = 0
        while i+1 < len(A) and A[i] < A[i+1]:
            i += 1
        j = len(A)-1
        while j-1 >= 0 and A[j-1] > A[j]:
            j -= 1
        return 0 < i == j < len(A)-1