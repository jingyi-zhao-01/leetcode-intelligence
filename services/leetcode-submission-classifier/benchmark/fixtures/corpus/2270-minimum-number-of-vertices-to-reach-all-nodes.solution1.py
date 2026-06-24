# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-number-of-vertices-to-reach-all-nodes
# source_path: LeetCode-Solutions-master/Python/minimum-number-of-vertices-to-reach-all-nodes.py
# solution_class: Solution
# submission_id: a4feb04bd745cbc299d40ca4fbfbb84354e49d02
# seed: 3564560999

# Time:  O(e)
# Space: O(n)

class Solution(object):
    def findSmallestSetOfVertices(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        result = []
        lookup = set()
        for u, v in edges:
            lookup.add(v)
        for i in xrange(n):
            if i not in lookup:
                result.append(i)
        return result