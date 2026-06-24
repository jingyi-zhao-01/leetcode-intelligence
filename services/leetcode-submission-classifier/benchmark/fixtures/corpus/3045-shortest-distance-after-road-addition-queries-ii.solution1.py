# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: shortest-distance-after-road-addition-queries-ii
# source_path: LeetCode-Solutions-master/Python/shortest-distance-after-road-addition-queries-ii.py
# solution_class: Solution
# submission_id: 2ad496f89a563e13bba08cfd0e7890805f91789c
# seed: 3541709738

# Time:  O(nlogn)
# Space: O(n)

from sortedcontainers import SortedList


# sorted list

class Solution(object):
    def shortestDistanceAfterQueries(self, n, queries):
        """
        :type n: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        sl = SortedList(xrange(n))
        result = []
        for u, v in queries:
            for i in reversed(xrange(sl.bisect_right(u), sl.bisect_left(v))): 
                sl.pop(i)
            result.append(len(sl)-1)
        return result