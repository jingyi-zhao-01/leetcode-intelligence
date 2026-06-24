# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: valid-arrangement-of-pairs
# source_path: LeetCode-Solutions-master/Python/valid-arrangement-of-pairs.py
# solution_class: Solution
# submission_id: c0393b80c6604a6f0e8d9e4ad0913aa6d6dd81a4
# seed: 1115292272

# Time:  O(|V| + |E|)
# Space: O(|V| + |E|)

import collections


# Hierholzer Algorithm

class Solution(object):
    def validArrangement(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: List[List[int]]
        """
        adj = collections.defaultdict(list)
        degree = collections.defaultdict(int)
        for u, v in pairs: 
            adj[u].append(v)
            degree[u] += 1
            degree[v] -= 1       
        result = []
        stk = [next((u for u, c in degree.iteritems() if c == 1), next(degree.iterkeys()))]
        while stk:
            while adj[stk[-1]]: 
                stk.append(adj[stk[-1]].pop())
            result.append(stk.pop())
        result.reverse()
        return [[result[i], result[i+1]] for i in xrange(len(result)-1)]