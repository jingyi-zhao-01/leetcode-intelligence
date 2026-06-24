# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: course-schedule-iv
# source_path: LeetCode-Solutions-master/Python/course-schedule-iv.py
# solution_class: Solution
# submission_id: b0d792bc3c1f2979b990624e2562d4f2003254b6
# seed: 1151932972

# Time:  O(n^3)
# Space: O(n^2)

class Solution(object):
    def checkIfPrerequisite(self, n, prerequisites, queries):
        """
        :type n: int
        :type prerequisites: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        def floydWarshall(n, graph): 
            reachable = set(map(lambda x: x[0]*n+x[1], graph)) 
            for k in xrange(n): 
                for i in xrange(n): 
                    for j in xrange(n): 
                        if i*n+j not in reachable and (i*n+k in reachable and k*n+j in reachable):
                            reachable.add(i*n+j)
            return reachable

        reachable = floydWarshall(n, prerequisites)
        return [i*n+j in reachable for i, j in queries]