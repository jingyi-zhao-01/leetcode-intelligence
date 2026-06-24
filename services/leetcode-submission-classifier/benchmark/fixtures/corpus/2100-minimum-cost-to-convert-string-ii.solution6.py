# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-cost-to-convert-string-ii
# source_path: LeetCode-Solutions-master/Python/minimum-cost-to-convert-string-ii.py
# solution_class: Solution6
# submission_id: 358f4048751916265ea2d786e8f2abb14fe4492b
# seed: 3639631652

# Time:  O(o * l + k * eloge + n * c * l), e is the number of edges reachable from a given node u, o = len(original), l = max(len(x) for x in original), k = len(lookups), c = len({len(x) for x in original})
# Space: O(o * l + k * v + c + l), v is the number of nodes reachable from a given node u

import collections
import itertools


# hash table, dijkstra's algorithm, dp, memoization

class Solution6(object):
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

        def floydWarshall(dist):
            for k in dist.iterkeys():
                for i in dist.iterkeys():
                    if dist[i][k] == INF:
                        continue
                    for j in dist.iterkeys():
                        if dist[k][j] == INF:
                            continue
                        dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])
        
        trie = Trie()
        buckets = collections.defaultdict(list)
        for x in itertools.chain(original, changed):
            not_duplicated, i = trie.add(x)
            if not_duplicated:
                buckets[len(x)].append(i)
        dists = {l:{u:{v:0 if u == v else INF for v in lookup} for u in lookup} for l, lookup in buckets.iteritems()}
        for i in xrange(len(original)):
            l = len(original[i])
            dist = dists[l]
            u, v = trie.query(original[i]), trie.query(changed[i])
            dist[u][v] = min(dist[u][v], cost[i])
        for dist in dists.itervalues():
            floydWarshall(dist)
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
                    dp[(j+1)%len(dp)] = min(dp[(j+1)%len(dp)], dp[i%len(dp)]+dists[j-i+1][trie.id(u)][trie.id(v)])
            dp[i%len(dp)] = INF
        return dp[len(source)%len(dp)] if dp[len(source)%len(dp)] != INF else -1