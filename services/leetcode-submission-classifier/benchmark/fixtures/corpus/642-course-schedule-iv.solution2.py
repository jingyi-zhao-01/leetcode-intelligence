# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: course-schedule-iv
# source_path: LeetCode-Solutions-master/Python/course-schedule-iv.py
# solution_class: Solution2
# submission_id: 3eaec86cd19700751988c207d9be4f0b8fc6c3f0
# seed: 1078092684

# Time:  O(n^3)
# Space: O(n^2)

class Solution2(object):
    def checkIfPrerequisite(self, n, prerequisites, queries):
        """
        :type n: int
        :type prerequisites: List[List[int]]
        :type queries: List[List[int]]
        :rtyp
        """
        graph = collections.defaultdict(list)
        for u, v in prerequisites:
            graph[u].append(v)
        result = []
        for i, j in queries:
            stk, lookup = [i], set([i])
            while stk:
                node = stk.pop()
                for nei in graph[node]:
                    if nei in lookup:
                        continue
                    stk.append(nei)
                    lookup.add(nei)
            result.append(j in lookup)
        return result