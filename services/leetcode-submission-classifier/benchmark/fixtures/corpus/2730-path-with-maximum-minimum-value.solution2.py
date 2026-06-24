# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: path-with-maximum-minimum-value
# source_path: LeetCode-Solutions-master/Python/path-with-maximum-minimum-value.py
# solution_class: Solution2
# submission_id: 3e22ecc807275cfde479c2b1fdc75977050f6281
# seed: 407172552

# Time:  O(m * n * log(m * n))
# Space: O(m * n)

# binary search + dfs solution

class Solution2(object):
    def maximumMinimumPath(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        max_heap = [(-A[0][0], 0, 0)]
        lookup = set([(0, 0)])
        while max_heap:
            i, r, c = heapq.heappop(max_heap)
            if r == len(A)-1 and c == len(A[0])-1:
                return -i
            for d in directions:
                nr, nc = r+d[0], c+d[1]
                if 0 <= nr < len(A) and \
                   0 <= nc < len(A[0]) and \
                   (nr, nc) not in lookup:
                    heapq.heappush(max_heap, (-min(-i, A[nr][nc]), nr, nc))
                    lookup.add((nr, nc))    
        return -1