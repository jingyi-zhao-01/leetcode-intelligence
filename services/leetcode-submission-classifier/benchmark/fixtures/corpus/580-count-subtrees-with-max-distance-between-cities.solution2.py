# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-subtrees-with-max-distance-between-cities
# source_path: LeetCode-Solutions-master/Python/count-subtrees-with-max-distance-between-cities.py
# solution_class: Solution2
# submission_id: c3a99330e03a7a82297f87edf8a919a1dd12ab01
# seed: 3658929119

# Time:  O(n^6)
# Space: O(n^3)

import collections

class Solution2(object):
    def countSubgraphsForEachDiameter(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        def popcount(mask):
            count = 0
            while mask:
                mask &= mask-1
                count += 1
            return count

        def bfs(adj, mask, start):
            q = collections.deque([(start, 0)])
            lookup = 1<<start
            count = popcount(mask)-1
            u, d = None, None
            while q:
                u, d = q.popleft()
                for v in adj[u]:
                    if not (mask&(1<<v)) or (lookup&(1<<v)):
                        continue
                    lookup |= 1<<v  
                    count -= 1
                    q.append((v, d+1))
            return count == 0, u, d
        
        def max_distance(n, edges, adj, mask):
            is_valid, farthest, _ = bfs(adj, mask, int(math.log(mask&-mask, 2)))
            return bfs(adj, mask, farthest)[-1] if is_valid else 0

        adj = collections.defaultdict(list)
        for u, v in edges:
            u -= 1
            v -= 1
            adj[u].append(v)
            adj[v].append(u)
        result = [0]*(n-1)
        for mask in xrange(1, 2**n):
            max_d = max_distance(n, edges, adj, mask)
            if max_d-1 >= 0:
                result[max_d-1] += 1
        return result