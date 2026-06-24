# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: smallest-string-with-swaps
# source_path: LeetCode-Solutions-master/Python/smallest-string-with-swaps.py
# solution_class: Solution
# submission_id: ca069a74e2c280ad329c4e412a1fb255ebc7ab3e
# seed: 4014659653

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

class Solution(object):
    def smallestStringWithSwaps(self, s, pairs):
        """
        :type s: str
        :type pairs: List[List[int]]
        :rtype: str
        """
        union_find = UnionFind(len(s))
        for x,y in pairs: 
            union_find.union_set(x, y)
        components = collections.defaultdict(list)
        for i in xrange(len(s)): 
            components[union_find.find_set(i)].append(s[i])
        for i in components.iterkeys(): 
            components[i].sort(reverse=True)
        result = []
        for i in xrange(len(s)): 
            result.append(components[union_find.find_set(i)].pop())
        return "".join(result)