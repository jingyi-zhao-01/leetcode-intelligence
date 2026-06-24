# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: relative-sort-array
# source_path: LeetCode-Solutions-master/Python/relative-sort-array.py
# solution_class: Solution
# submission_id: 8e1e3c115589385be1520ada05e800a7c6316c14
# seed: 954393404

# Time:  O(nlogn)
# Space: O(n)

class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        lookup = {v: i for i, v in enumerate(arr2)}
        return sorted(arr1, key=lambda i: lookup.get(i, len(arr2)+i))