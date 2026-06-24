# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-xor-of-two-non-overlapping-subtrees
# source_path: LeetCode-Solutions-master/Python/maximum-xor-of-two-non-overlapping-subtrees.py
# solution_class: Solution2
# submission_id: 331d9a7b77d03e4f45ad482930d7ebc544e58758
# seed: 1067741844

# Time:  O(nlogr), r is sum(values)
# Space: O(n)

# iterative dfs, trie, greedy
class Trie(object):
    def __init__(self, bit_length):
        self.__root = {}
        self.__bit_length = bit_length
        
    def insert(self, num):
        node = self.__root
        for i in reversed(xrange(self.__bit_length)):
            curr = (num>>i) & 1
            if curr not in node:
                node[curr] = {}
            node = node[curr]
                
    def query(self, num):
        if not self.__root: 
            return -1
        node, result = self.__root, 0
        for i in reversed(xrange(self.__bit_length)):
            curr = (num>>i) & 1
            if 1^curr in node:
                node = node[1^curr]
                result |= 1<<i
            else:
                node = node[curr]
        return result

class Solution2(object):
    def maxXor(self, n, edges, values):
        """
        :type n: int
        :type edges: List[List[int]]
        :type values: List[int]
        :rtype: int
        """
        def dfs(u, p):
            lookup[u] = values[u]+sum(dfs(v, u) for v in adj[u] if v != p)
            return lookup[u]

        def dfs2(u, p):
            result = max(trie.query(lookup[u]), 0)
            for v in adj[u]:
                if v == p:
                    continue
                result = max(result, dfs2(v, u))
            trie.insert(lookup[u])
            return result
        
        adj = [[] for _ in xrange(len(values))]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        lookup = [0]*len(values)
        dfs(0, -1)
        trie = Trie(lookup[0].bit_length())
        return dfs2(0, -1)