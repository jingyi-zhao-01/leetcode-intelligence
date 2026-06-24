# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-genetic-difference-query
# source_path: LeetCode-Solutions-master/Python/maximum-genetic-difference-query.py
# solution_class: Solution2
# submission_id: 72f2daecb867a193bba1c6c8fd84d0a723408a7a
# seed: 4172447573

# Time:  O(nlogk + mlogk), k is max(max(vals), n-1)
# Space: O(n + logk)

import collections


class Trie(object):
    def __init__(self, bit_count):
        self.__root = {}
        self.__bit_count = bit_count
        
    def insert(self, num, v):
        node = self.__root
        for i in reversed(xrange(self.__bit_count)):
            curr = (num>>i) & 1
            new_node = node.setdefault(curr, collections.defaultdict(int))
            new_node["_cnt"] += v
            if not new_node["_cnt"]:
                del node[curr]
                break
            node = new_node
                
    def query(self, num):
        node, result = self.__root, 0
        for i in reversed(xrange(self.__bit_count)):
            curr = (num>>i) & 1
            if 1^curr in node:
                node = node[1^curr]
                result |= 1<<i
            else:
                node = node[curr]
        return result

class Solution2(object):
    def maxGeneticDifference(self, parents, queries):
        """
        :type parents: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        def dfs(adj, qs, node, trie, result):
            trie.insert(node, 1)
            for i, val in qs[node]:
                result[i] = trie.query(val)
            for child in adj[node]:
                dfs(adj, qs, child, trie, result)
            trie.insert(node, -1)

        adj = collections.defaultdict(list)
        for node, parent in enumerate(parents):
            adj[parent].append(node)
        qs = collections.defaultdict(list)
        max_val = len(parents)-1
        for i, (node, val) in enumerate(queries):
            qs[node].append((i, val))
            max_val = max(max_val, val)
        result = [0]*len(queries)
        dfs(adj, qs, adj[-1][0], Trie(max_val.bit_length()), result)
        return result