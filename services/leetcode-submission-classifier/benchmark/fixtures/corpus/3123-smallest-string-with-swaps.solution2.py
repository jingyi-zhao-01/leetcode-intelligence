# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: smallest-string-with-swaps
# source_path: LeetCode-Solutions-master/Python/smallest-string-with-swaps.py
# solution_class: Solution2
# submission_id: ece36ab307d6e6de68abb5e63289081bce273f7f
# seed: 1084054958

# Time:  O(nlogn)
# Space: O(n)

import collections


class UnionFind(object):
    def __init__(self, n):
        self.set = range(n)

    def find_set(self, x):
        if self.set[x] != x:
            self.set[x] = self.find_set(self.set[x])  # path compression.
        return self.set[x]

    def union_set(self, x, y):
        x_root, y_root = map(self.find_set, (x, y))
        if x_root == y_root:
            return False
        self.set[max(x_root, y_root)] = min(x_root, y_root)
        return True

class Solution2(object):
    def smallestStringWithSwaps(self, s, pairs):
        """
        :type s: str
        :type pairs: List[List[int]]
        :rtype: str
        """
        def dfs(i, adj, lookup, component):
            lookup.add(i)
            component.append(i)
            for j in adj[i]:
                if j in lookup:
                    continue
                dfs(j, adj, lookup, component)
            
        adj = collections.defaultdict(list)
        for i, j in pairs:
            adj[i].append(j)
            adj[j].append(i)
        lookup = set()
        result = list(s)
        for i in xrange(len(s)):
            if i in lookup:
                continue
            component = []
            dfs(i, adj, lookup, component)
            component.sort()
            chars = sorted(result[k] for k in component)
            for comp, char in itertools.izip(component, chars):
                result[comp] = char
        return "".join(result)