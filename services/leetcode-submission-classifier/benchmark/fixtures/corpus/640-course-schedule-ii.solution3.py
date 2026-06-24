# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: course-schedule-ii
# source_path: LeetCode-Solutions-master/Python/course-schedule-ii.py
# solution_class: Solution3
# submission_id: de4254724847ee3e9fdafef266820e802db788f9
# seed: 4238514

# Time:  O(|V| + |E|)
# Space: O(|E|)

import collections


# Khan's algorithm (bfs solution)

class Solution3(object):
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
            adj[u].append(v)
        lookup = collections.defaultdict(lambda:WHITE)
        for u in xrange(numCourses):
            if not dfs(u):
                return []
        return result