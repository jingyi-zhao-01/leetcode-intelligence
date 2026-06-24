# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: check-array-formation-through-concatenation
# source_path: LeetCode-Solutions-master/Python/check-array-formation-through-concatenation.py
# solution_class: Solution
# submission_id: c108e43539d235503632edc2b3a5d0d267d36152
# seed: 3417653526

# Time:  O(n)
# Space: O(n)

class Solution(object):
    def canFormArray(self, arr, pieces):
        """
        :type arr: List[int]
        :type pieces: List[List[int]]
        :rtype: bool
        """
        lookup = {x[0]: i for i, x in enumerate(pieces)}
        i = 0
        while i < len(arr): 
            if arr[i] not in lookup:
                return False
            for c in pieces[lookup[arr[i]]]:
                if i == len(arr) or arr[i] != c:
                    return False
                i += 1
        return True 