# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: course-schedule-ii
# source_path: LeetCode-Solutions-master/Python/course-schedule-ii.py
# solution_class: Solution
# submission_id: 69337f69afdab26eff4e11d57bad07b71c74a2ee
# seed: 1354814501

# Time:  O(|V| + |E|)
# Space: O(|E|)

import collections


# Khan's algorithm (bfs solution)

class Solution(object):
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
        q = [u for u in xrange(numCourses) if u not in in_degree]
        while q:
            new_q = []
            for u in q:
                result.append(u)
                for v in adj[u]:
                    in_degree[v] -= 1
                    if in_degree[v] == 0:
                        new_q.append(v)
            q = new_q
        return result if len(result) == numCourses else []