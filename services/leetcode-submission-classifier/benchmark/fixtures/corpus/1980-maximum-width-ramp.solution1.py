# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-width-ramp
# source_path: LeetCode-Solutions-master/Python/maximum-width-ramp.py
# solution_class: Solution
# submission_id: 639ac5854c4dc6cfb104acedb8b495bdf072ca9b
# seed: 1129726566

# Time:  O(n)
# Space: O(n)

class Solution(object):
    def maxWidthRamp(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        result = 0
        s = []
        for i in A:
            if not s or A[s[-1]] > A[i]:
                s.append(i)
        for j in reversed(xrange(len(A))):
            while s and A[s[-1]] <= A[j]:
                result = max(result, j-s.pop())
        return result