# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: course-schedule-ii
# source_path: LeetCode-Solutions-master/Python/course-schedule-ii.py
# solution_class: Solution2
# submission_id: 28922d2fbf4b229f34a1784a2944a35e97444ab2
# seed: 865146606

# Time:  O(|V| + |E|)
# Space: O(|E|)

import collections


# Khan's algorithm (bfs solution)

class Solution2(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        adj = collections.defaultdict(list)
        in_degree = collections.Counter()
        for u, v in prerequisites:
            in_degree[u] += 1
            adj[v].append(u)
        result = []
        stk = [u for u in xrange(numCourses) if u not in in_degree]
        while stk:
            u = stk.pop()
            result.append(u)
            for v in adj[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    stk.append(v)
        return result if len(result) == numCourses else []