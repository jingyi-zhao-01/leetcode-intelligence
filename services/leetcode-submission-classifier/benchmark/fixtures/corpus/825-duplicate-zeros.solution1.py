# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: duplicate-zeros
# source_path: LeetCode-Solutions-master/Python/duplicate-zeros.py
# solution_class: Solution
# submission_id: deeb7decbb998ce795d91894517db607fc524c8f
# seed: 3804506031

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        shift, i = 0, 0
        while i+shift < len(arr):
            shift += int(arr[i] == 0)
            i += 1
        i -= 1
        while shift:
            if i+shift < len(arr):
                arr[i+shift] = arr[i]
            if arr[i] == 0:
                shift -= 1
                arr[i+shift] = arr[i]
            i -= 1