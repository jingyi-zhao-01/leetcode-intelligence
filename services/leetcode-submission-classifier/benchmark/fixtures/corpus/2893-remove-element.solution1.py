# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: remove-element
# source_path: LeetCode-Solutions-master/Python/remove-element.py
# solution_class: Solution
# submission_id: 47c96282c998b5f0a746ea2502eac5483572ffd1
# seed: 53378960

# Time:  O(n)
# Space: O(1)

class Solution(object):
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        i, last = 0, len(A) - 1
        while i <= last:
            if A[i] == elem:
                A[i], A[last] = A[last], A[i]
                last -= 1
            else:
                i += 1
        return last + 1