# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: trapping-rain-water
# source_path: LeetCode-Solutions-master/Python/trapping-rain-water.py
# solution_class: Solution2
# submission_id: a733b4fb14f13614ad5d439ecceb1f24e66ba556
# seed: 2879817000

# Time:  O(n)
# Space: O(1)

class Solution2(object):
    # @param A, a list of integers
    # @return an integer
    def trap(self, A):
        result = 0
        top = 0
        for i in xrange(len(A)):
            if A[top] < A[i]:
                top = i

        second_top = 0
        for i in xrange(top):
            if A[second_top] < A[i]:
                second_top = i
            result += A[second_top] - A[i]

        second_top = len(A) - 1
        for i in reversed(xrange(top, len(A))):
            if A[second_top] < A[i]:
                second_top = i
            result += A[second_top] - A[i]

        return result