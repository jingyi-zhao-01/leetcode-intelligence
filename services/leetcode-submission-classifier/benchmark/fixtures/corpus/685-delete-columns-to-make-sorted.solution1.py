# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: delete-columns-to-make-sorted
# source_path: LeetCode-Solutions-master/Python/delete-columns-to-make-sorted.py
# solution_class: Solution
# submission_id: 36e9214d71efda424cb9226ba8a4c613c3366f6e
# seed: 138549356

# Time:  O(n * l)
# Space: O(1)

class Solution(object):
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        result = 0
        for c in xrange(len(A[0])):
            for r in xrange(1, len(A)):
                if A[r-1][c] > A[r][c]:
                    result += 1
                    break
        return result