# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-nodes-in-the-sub-tree-with-the-same-label
# source_path: LeetCode-Solutions-master/Python/number-of-nodes-in-the-sub-tree-with-the-same-label.py
# solution_class: Solution2
# submission_id: 19f03e134a11346c40059ba1c46a6c3a82bc4489
# seed: 1548988009

# Time:  O(n)
# Space: O(h)

class Solution2(object):
    def countSubTrees(self, n, edges, labels):
        """
        :type n: int
        :type edges: List[List[int]]
        :type labels: str
        :rtype: List[int]
        """
        def dfs(labels, adj, node, parent, result):
            count = [0]*26
            for child in adj[node]:
                if child == parent:
                    continue
                new_count = dfs(labels, adj, child, node, result)
                for k in xrange(len(new_count)):
                    count[k] += new_count[k]
            count[ord(labels[node]) - ord('a')] += 1
            result[node] = count[ord(labels[node]) - ord('a')]
            return count
        
        adj = [[] for _ in xrange(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        result = [0]*n
        dfs(labels, adj, 0, -1, result)
        return result