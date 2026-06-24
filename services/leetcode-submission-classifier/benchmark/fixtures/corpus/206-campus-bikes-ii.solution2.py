# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: campus-bikes-ii
# source_path: LeetCode-Solutions-master/Python/campus-bikes-ii.py
# solution_class: Solution2
# submission_id: 0b13432c007667403b85b463a60c3c92a3fd7fde
# seed: 1354709477

# Time:  O(w * b * 2^b)
# Space: O(b * 2^b)

# if w = b, we can even apply Hungarian algorithm (see https://en.wikipedia.org/wiki/Hungarian_algorithm),
# it can be improved to O(w^3), see https://github.com/t3nsor/codebook/blob/master/bipartite-mincost.cpp

class Solution2(object):
    def assignBikes(self, workers, bikes):
        """
        :type workers: List[List[int]]
        :type bikes: List[List[int]]
        :rtype: int
        """
        def manhattan(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        
        min_heap = [(0, 0, 0)]
        lookup = set()
        while min_heap:
            cost, i, taken = heapq.heappop(min_heap)
            if (i, taken) in lookup:
                continue
            lookup.add((i, taken))
            if i == len(workers):
                return cost
            for j in xrange(len(bikes)):
                if taken & (1<<j):
                    continue
                heapq.heappush(min_heap, (cost+manhattan(workers[i], bikes[j]),  # O(b)
                                          i+1,            # O(w)
                                          taken|(1<<j)))  # O(2^b)