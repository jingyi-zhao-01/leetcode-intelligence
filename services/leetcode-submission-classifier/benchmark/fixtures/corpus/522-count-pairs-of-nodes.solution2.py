# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-pairs-of-nodes
# source_path: LeetCode-Solutions-master/Python/count-pairs-of-nodes.py
# solution_class: Solution2
# submission_id: 17a0ebe0563d9b7ca900e6537dfec4a08f1c78f5
# seed: 777412144

# Time:  O(n + e + q)
# Space: O(n + e)

import collections
import itertools


# pure counting solution

class Solution2(object):
    def countPairs(self, n, edges, queries):
        """
        :type n: int
        :type edges: List[List[int]]
        :type queries: List[int]
        :rtype: List[int]
        """
        degree = [0]*(n+1)
        shared = collections.Counter((min(n1, n2), max(n1, n2)) for n1, n2 in edges)
        for n1, n2 in edges:
            degree[n1] += 1
            degree[n2] += 1
        sorted_degree = sorted(degree)
        result = []
        for k, q in enumerate(queries):
            left, right = 1, n
            cnt = 0
            while left < right:
                if q < sorted_degree[left]+sorted_degree[right]:
                    cnt += right-left
                    right -= 1
                else:
                    left += 1
            for (i, j), shared_degree in shared.iteritems():
                if degree[i]+degree[j]-shared_degree <= q < degree[i]+degree[j]:
                    cnt -= 1
            result.append(cnt)
        return result