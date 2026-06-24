# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: parallel-courses
# source_path: LeetCode-Solutions-master/Python/parallel-courses.py
# solution_class: Solution
# submission_id: 697ae61bc94b9c04e4f16861c8c700a9cadec81c
# seed: 1402997817

# Time:  O(|V| + |E|)
# Space: O(|E|)

import collections

class Solution(object):
    def minimumSemesters(self, N, relations):
        """
        :type N: int
        :type relations: List[List[int]]
        :rtype: int
        """
        g = collections.defaultdict(list)
        in_degree = [0]*N
        for x, y in relations:
            g[x-1].append(y-1)
            in_degree[y-1] += 1
        q = collections.deque([(1, i) for i in xrange(N) if not in_degree[i]])

        result = 0
        count = N
        while q:
            level, u = q.popleft()
            count -= 1
            result = level
            for v in g[u]:
                in_degree[v] -= 1
                if not in_degree[v]:
                    q.append((level+1, v))
        return result if count == 0 else -1