# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: remove-duplicates-from-sorted-array
# source_path: LeetCode-Solutions-master/Python/remove-duplicates-from-sorted-array.py
# solution_class: Solution
# submission_id: c7c96360b41ecaf98b967c5e587ca824bc081891
# seed: 1099956178

# Time:  O(n)
# Space: O(1)

class Solution(object):
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if not A:
            return 0

        last = 0
        for i in xrange(len(A)):
            if A[last] != A[i]:
                last += 1
                A[last] = A[i]
        return last + 1