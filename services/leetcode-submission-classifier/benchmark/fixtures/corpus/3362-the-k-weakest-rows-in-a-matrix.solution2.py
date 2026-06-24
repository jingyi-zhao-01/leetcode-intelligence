# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: the-k-weakest-rows-in-a-matrix
# source_path: LeetCode-Solutions-master/Python/the-k-weakest-rows-in-a-matrix.py
# solution_class: Solution2
# submission_id: 46859c07739c8f0ae351c89e5f8513229c391e2f
# seed: 4125547153

# Time:  O(m * n)
# Space: O(k)

class Solution2(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        lookup = collections.OrderedDict()
        for j in xrange(len(mat[0])):
            for i in xrange(len(mat)):
                if mat[i][j] or i in lookup:
                    continue
                lookup[i] = True
                if len(lookup) == k:
                    return lookup.keys()
        for i in xrange(len(mat)):
            if i in lookup:
                continue
            lookup[i] = True
            if len(lookup) == k:
                break
        return lookup.keys()