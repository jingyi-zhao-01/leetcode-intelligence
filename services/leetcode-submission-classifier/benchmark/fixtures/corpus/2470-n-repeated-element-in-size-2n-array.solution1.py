# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: n-repeated-element-in-size-2n-array
# source_path: LeetCode-Solutions-master/Python/n-repeated-element-in-size-2n-array.py
# solution_class: Solution
# submission_id: 30c872d63aab7f92f4bb952713997de9107c8890
# seed: 2312685300

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        for i in xrange(2, len(A)):
            if A[i-1] == A[i] or A[i-2] == A[i]:
                return A[i]
        return A[0]