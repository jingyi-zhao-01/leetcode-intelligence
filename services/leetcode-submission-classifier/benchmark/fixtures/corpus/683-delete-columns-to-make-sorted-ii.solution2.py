# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: delete-columns-to-make-sorted-ii
# source_path: LeetCode-Solutions-master/Python/delete-columns-to-make-sorted-ii.py
# solution_class: Solution2
# submission_id: be03274563d69b6bfe9d350f43f1a9acd018ae69
# seed: 2154733051

# Time:  O(n * l)
# Space: O(n)

class Solution2(object):
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        result = 0
        is_sorted = [False]*(len(A)-1)
        for j in xrange(len(A[0])):
            tmp = is_sorted[:]
            for i in xrange(len(A)-1):
                if A[i][j] > A[i+1][j] and tmp[i] == False:
                    result += 1
                    break
                if A[i][j] < A[i+1][j]:
                    tmp[i] = True
            else:
                is_sorted = tmp
        return result