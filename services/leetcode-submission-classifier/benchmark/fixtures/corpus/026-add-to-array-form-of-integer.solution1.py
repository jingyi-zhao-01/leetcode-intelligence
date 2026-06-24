# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: add-to-array-form-of-integer
# source_path: LeetCode-Solutions-master/Python/add-to-array-form-of-integer.py
# solution_class: Solution
# submission_id: 739b46b6b2d0a87746d07cd2a9bb342246ab1d1e
# seed: 575441303

# Time:  O(n + logk)
# Space: O(1)

class Solution(object):
    def addToArrayForm(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        A.reverse()
        carry, i = K, 0
        A[i] += carry
        carry, A[i] = divmod(A[i], 10)
        while carry:
            i += 1
            if i < len(A):
                A[i] += carry
            else:
                A.append(carry)
            carry, A[i] = divmod(A[i], 10)
        A.reverse()
        return A