# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: remove-duplicates-from-sorted-array-ii
# source_path: LeetCode-Solutions-master/Python/remove-duplicates-from-sorted-array-ii.py
# solution_class: Solution
# submission_id: e4c0356f51141d45c00566f5bc43508f8ed6dabf
# seed: 1751336335

# Time:  O(n)
# Space: O(1)

class Solution(object):
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if not A:
            return 0

        last, i, same = 0, 1, False
        while i < len(A):
            if A[last] != A[i] or not same:
                same = A[last] == A[i]
                last += 1
                A[last] = A[i]
            i += 1

        return last + 1