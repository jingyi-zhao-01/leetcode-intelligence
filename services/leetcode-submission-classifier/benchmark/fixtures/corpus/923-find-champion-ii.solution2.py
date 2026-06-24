# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-champion-ii
# source_path: LeetCode-Solutions-master/Python/find-champion-ii.py
# solution_class: Solution2
# submission_id: 8848c398131c6203a7dc03e6a2ce16a09dad5f86
# seed: 1614197031

# Time:  O(n)
# Space: O(n)

# graph, hash table

class Solution2(object):
    def findChampion(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        lookup = {v for _, v in edges}
        return next(u for u in xrange(n) if u not in lookup) if len(lookup) == n-1 else -1