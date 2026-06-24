# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: course-schedule
# source_path: LeetCode-Solutions-master/Python/course-schedule.py
# solution_class: Solution2
# submission_id: 9b80d43544a71920910cce517a2e891ddeba1b38
# seed: 2334011572

# Time:  O(|V| + |E|)
# Space: O(|E|)

import collections


# Khan's algorithm (bfs solution)

class Solution2(object):
    def canFinish(self, numCourses, prerequisites):
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
        return len(result) == numCourses