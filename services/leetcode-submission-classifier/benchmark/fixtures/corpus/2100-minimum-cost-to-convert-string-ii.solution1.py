# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-cost-to-convert-string-ii
# source_path: LeetCode-Solutions-master/Python/minimum-cost-to-convert-string-ii.py
# solution_class: Solution
# submission_id: 1fd770b0c0c5454278b8c803322fb63c7a62c89c
# seed: 73038937

# Time:  O(o * l + k * eloge + n * c * l), e is the number of edges reachable from a given node u, o = len(original), l = max(len(x) for x in original), k = len(lookups), c = len({len(x) for x in original})
# Space: O(o * l + k * v + c + l), v is the number of nodes reachable from a given node u

import collections
import itertools


# hash table, dijkstra's algorithm, dp, memoization

class Solution(object):
    def minimumCost(self, source, target, original, changed, cost):
        """
        :type source: str
        :type target: str
        :type original: List[str]
        :type changed: List[str]
        :type cost: List[int]
        :rtype: int
        """
        INF = float("inf")
        lookups = collections.defaultdict(dict)
        for x in itertools.chain(original, changed):
            l = len(x)
            lookup = lookups[l]
            if x not in lookup:
                lookup[x] = len(lookup)
        def dijkstra(dist, start):
            best = [INF]*len(dist)
            best[start] = 0
            min_heap = [(0, start)]
            while min_heap:
                curr, u = heapq.heappop(min_heap)
                if curr > best[u]:
                    continue
                for v, w in enumerate(dist[u]):     
                    if best[v] <= curr+w:
                        continue
                    best[v] = curr+w
                    heapq.heappush(min_heap, (best[v], v))
            return best

        memo = {}
        def memoization(l, dist, u, v):
            if l not in memo:
                memo[l] = {}
            if u not in memo[l]:
                memo[l][u] = dijkstra(dist, u)
            return memo[l][u][v]

        dists = {l:[[0 if u == v else INF for v in xrange(len(lookup))] for u in xrange(len(lookup))] for l, lookup in lookups.iteritems()}
        for i in xrange(len(original)):
            l = len(original[i])
            lookup, dist = lookups[l], dists[l]
            u, v = lookup[original[i]], lookup[changed[i]]
            dist[u][v] = min(dist[u][v], cost[i])
        candidates = {len(x) for x in original}
        dp = [INF]*(max(len(x) for x in original)+1)
        dp[0] = 0
        for i in xrange(len(source)):
            if dp[i%len(dp)] == INF:
                continue
            if source[i] == target[i]:
                dp[(i+1)%len(dp)] = min(dp[(i+1)%len(dp)], dp[i%len(dp)])
            for l in candidates:
                if i+l > len(source):
                    continue
                lookup, dist = lookups[l], dists[l]
                u, v = source[i:i+l], target[i:i+l]
                if u in lookup and v in lookup:
                    dp[(i+l)%len(dp)] = min(dp[(i+l)%len(dp)], dp[i%len(dp)]+memoization(l, dist, lookup[u], lookup[v]))
            dp[i%len(dp)] = INF
        return dp[len(source)%len(dp)] if dp[len(source)%len(dp)] != INF else -1