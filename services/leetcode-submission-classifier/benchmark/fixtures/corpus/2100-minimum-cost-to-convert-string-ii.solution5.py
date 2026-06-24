# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-cost-to-convert-string-ii
# source_path: LeetCode-Solutions-master/Python/minimum-cost-to-convert-string-ii.py
# solution_class: Solution5
# submission_id: 0d598341e026978e2644498a854e3deb2eccebf9
# seed: 315859706

# Time:  O(o * l + k * eloge + n * c * l), e is the number of edges reachable from a given node u, o = len(original), l = max(len(x) for x in original), k = len(lookups), c = len({len(x) for x in original})
# Space: O(o * l + k * v + c + l), v is the number of nodes reachable from a given node u

import collections
import itertools


# hash table, dijkstra's algorithm, dp, memoization

class Solution5(object):
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
        class Trie(object):
            def __init__(self):
                self.__nodes = []
                self.__idxs = []
                self.k = 0
                self.__new_node()
            
            def __new_node(self):
                self.__nodes.append([-1]*26)
                self.__idxs.append(-1)
                return len(self.__nodes)-1

            def add(self, s):
                curr = 0
                for c in s:
                    x = ord(c)-ord('a')
                    if self.__nodes[curr][x] == -1:
                        self.__nodes[curr][x] = self.__new_node()
                    curr = self.__nodes[curr][x]
                if self.__idxs[curr] == -1:
                    self.__idxs[curr] = self.k
                    self.k += 1
                    return True, self.__idxs[curr]
                return False, self.__idxs[curr]
            
            def query(self, s):
                curr = 0
                for c in s:
                    curr = self.__nodes[curr][ord(c)-ord('a')]
                return self.__idxs[curr]
    
            def next(self, curr, c):
                return self.__nodes[curr][ord(c)-ord('a')]

            def id(self, curr):
                return self.__idxs[curr]

        trie = Trie()
        for x in itertools.chain(original, changed):
            trie.add(x)
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
            if u not in memo:
                memo[u] = dijkstra(u)
            return memo[u][v] if v in memo[u] else INF

        dist = {}
        for i in xrange(len(original)):
            u, v = trie.query(original[i]), trie.query(changed[i])
            if u not in dist:
                dist[u] = {v:INF}
            if v not in dist[u]:
                dist[u][v] = INF
            dist[u][v] = min(dist[u][v], cost[i])
        dp = [INF]*(max(len(x) for x in original)+1)
        dp[0] = 0
        for i in xrange(len(source)):
            if dp[i%len(dp)] == INF:
                continue
            if source[i] == target[i]:
                dp[(i+1)%len(dp)] = min(dp[(i+1)%len(dp)], dp[i%len(dp)])
            u = v = 0
            for j in xrange(i, len(source)):
                u = trie.next(u, source[j])
                v = trie.next(v, target[j])
                if u == -1 or v == -1:
                    break
                if trie.id(u) != -1 and trie.id(v) != -1:
                    dp[(j+1)%len(dp)] = min(dp[(j+1)%len(dp)], dp[i%len(dp)]+memoization(trie.id(u), trie.id(v)))
            dp[i%len(dp)] = INF
        return dp[len(source)%len(dp)] if dp[len(source)%len(dp)] != INF else -1