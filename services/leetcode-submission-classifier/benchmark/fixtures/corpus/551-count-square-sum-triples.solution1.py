# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-square-sum-triples
# source_path: LeetCode-Solutions-master/Python/count-square-sum-triples.py
# solution_class: Solution
# submission_id: 516ad333ab97fed66c50ba323e223c59b93ede3d
# seed: 1305889605

# Time:  O(n^2)
# Space: O(n)

class Solution(object):
    def countTriples(self, n):
        """
        :type n: int
        :rtype: int
        """
        lookup = set()
        for i in xrange(1, n+1):
            lookup.add(i**2)
        result = 0
        for i in xrange(1, n+1):
            for j in xrange(1, n+1):
                result += int(i**2+j**2 in lookup)
        return result