# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: sort-array-by-parity-ii
# source_path: LeetCode-Solutions-master/Python/sort-array-by-parity-ii.py
# solution_class: Solution
# submission_id: c43d231ce062ffece99bb977b2aa0af9bbce41ce
# seed: 3239897201

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        j = 1
        for i in xrange(0, len(A), 2):
            if A[i] % 2:
                while A[j] % 2:
                    j += 2
                A[i], A[j] = A[j], A[i]
        return A