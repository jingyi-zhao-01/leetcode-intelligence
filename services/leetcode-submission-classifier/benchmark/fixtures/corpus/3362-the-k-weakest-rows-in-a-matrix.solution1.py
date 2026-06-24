# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: the-k-weakest-rows-in-a-matrix
# source_path: LeetCode-Solutions-master/Python/the-k-weakest-rows-in-a-matrix.py
# solution_class: Solution
# submission_id: e289b3349ca8ecd782fe4d49fe2b2345ed05addd
# seed: 275130002

# Time:  O(m * n)
# Space: O(k)

class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        result, lookup = [], set()
        for j in xrange(len(mat[0])):
            for i in xrange(len(mat)):
                if mat[i][j] or i in lookup:
                    continue
                lookup.add(i)
                result.append(i)
                if len(result) == k:
                    return result
        for i in xrange(len(mat)):
            if i in lookup:
                continue
            lookup.add(i)
            result.append(i)
            if len(result) == k:
                break
        return result