# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: delete-columns-to-make-sorted-ii
# source_path: LeetCode-Solutions-master/Python/delete-columns-to-make-sorted-ii.py
# solution_class: Solution
# submission_id: d212df9f8d209696717573b03bce68abefa334cb
# seed: 1948467945

# Time:  O(n * l)
# Space: O(n)

class Solution(object):
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        result = 0
        unsorted = set(range(len(A)-1))
        for j in xrange(len(A[0])):
            if any(A[i][j] > A[i+1][j] for i in unsorted):
                result += 1
            else:
                unsorted -= set(i for i in unsorted if A[i][j] < A[i+1][j])
        return result