# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-artifacts-that-can-be-extracted
# source_path: LeetCode-Solutions-master/Python/count-artifacts-that-can-be-extracted.py
# solution_class: Solution
# submission_id: 638d46e5d4e1f435f29db835994b2b9e2f56c182
# seed: 1259347693

# Time:  O(a + d), a is the number of grids covered by artifacts, d is the size of dig
# Space: O(d)

# hash table

class Solution(object):
    def digArtifacts(self, n, artifacts, dig):
        """
        :type n: int
        :type artifacts: List[List[int]]
        :type dig: List[List[int]]
        :rtype: int
        """
        lookup = set(map(tuple, dig))
        return sum(all((i, j) in lookup for i in xrange(r1, r2+1) for j in xrange(c1, c2+1)) for r1, c1, r2, c2 in artifacts)