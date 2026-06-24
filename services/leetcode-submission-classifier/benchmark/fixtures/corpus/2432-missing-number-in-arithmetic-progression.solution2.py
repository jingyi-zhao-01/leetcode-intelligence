# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: missing-number-in-arithmetic-progression
# source_path: LeetCode-Solutions-master/Python/missing-number-in-arithmetic-progression.py
# solution_class: Solution2
# submission_id: 998199fd230ac8c102250cbb0b8aaf2ad4cb4a73
# seed: 2550893882

# Time:  O(logn)
# Space: O(1)

class Solution2(object):
    def missingNumber(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        return (min(arr)+max(arr))*(len(arr)+1)//2 - sum(arr)