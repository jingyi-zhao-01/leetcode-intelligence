# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-cost-to-convert-string-ii
# source_path: LeetCode-Solutions-master/Python/minimum-cost-to-convert-string-ii.py
# solution_class: Solution3
# submission_id: 7fbe3e421e97959e624ac71ab99b7e48b450dd0c
# seed: 1036499145

# Time:  O(o * l + k * eloge + n * c * l), e is the number of edges reachable from a given node u, o = len(original), l = max(len(x) for x in original), k = len(lookups), c = len({len(x) for x in original})
# Space: O(o * l + k * v + c + l), v is the number of nodes reachable from a given node u

import collections
import itertools


# hash table, dijkstra's algorithm, dp, memoization

class Solution3(object):
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

        lookup = {}
        for x in itertools.chain(original, changed):
            if x in lookup:
                continue
            lookup[x] = len(lookup)
        def dijkstra(start):
            best = {start:0}
            min_heap = [(0, start)]
            while min_heap:
                curr, u = heapq.heappop(min_heap)
                if curr > best[u]:
                    continue
                if u not in dist:
                    continue
                for v, w in dist[u].iteritems():     
                    if v in best and best[v] <= curr+w:
                        continue
                    best[v] = curr+w
                    heapq.heappush(min_heap, (best[v], v))
            return best

        memo = {}
        def memoization(u, v):
            if u not in lookup:
                memo[u] = dijkstra(u)
            return memo[u][v] if v in memo[u] else INF

        dist = {}
        for i in xrange(len(original)):
            u, v = lookup[original[i]], lookup[changed[i]]
            if u not in dist:
                dist[u] = {v:INF}
            if v not in dist[u]:
                dist[u][v] = INF
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
                u, v = source[i:i+l], target[i:i+l]
                if u in lookup and v in lookup:
                    dp[(i+l)%len(dp)] = min(dp[(i+l)%len(dp)], dp[i%len(dp)]+memoization(lookup[u], lookup[v]))
            dp[i%len(dp)] = INF
        return dp[len(source)%len(dp)] if dp[len(source)%len(dp)] != INF else -1