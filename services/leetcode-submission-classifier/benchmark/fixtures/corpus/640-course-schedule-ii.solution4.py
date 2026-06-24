# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: course-schedule-ii
# source_path: LeetCode-Solutions-master/Python/course-schedule-ii.py
# solution_class: Solution4
# submission_id: f226071ad89471c3c2b0dae4c24f4c1a72ea15a7
# seed: 2742265354

# Time:  O(|V| + |E|)
# Space: O(|E|)

import collections


# Khan's algorithm (bfs solution)

class Solution4(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        WHITE, GRAY, BLACK = range(3)
        def dfs(u):
            if lookup[u] != WHITE:
                return lookup[u] == BLACK
            lookup[u] = GRAY
            if any(not dfs(v) for v in adj[u]):
                return False
            lookup[u] = BLACK
            result.append(u)  # should be postorder
            return True

        result = []
        adj = collections.defaultdict(list)
        for u, v in prerequisites:
            adj[v].append(u)
        lookup = collections.defaultdict(lambda:WHITE)
        for u in xrange(numCourses):
            if not dfs(u):
                return []
        result.reverse()
        return result