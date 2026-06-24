# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: smallest-rotation-with-highest-score
# source_path: LeetCode-Solutions-master/Python/smallest-rotation-with-highest-score.py
# solution_class: Solution
# submission_id: 13427c8983dad236d049fe46742bc0512fcb85fc
# seed: 2229127582

# Time:  O(n)
# Space: O(n)

class Solution(object):
    def bestRotation(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        N = len(A)
        change = [1] * N
        for i in xrange(N):
            change[(i-A[i]+1)%N] -= 1
        for i in xrange(1, N):
            change[i] += change[i-1]
        return change.index(max(change))