# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-the-number-of-good-nodes
# source_path: LeetCode-Solutions-master/Python/count-the-number-of-good-nodes.py
# solution_class: Solution2
# submission_id: ebdc9128e4af10ecdd18b2cc47bca81b7e79c119
# seed: 3049559296

# Time:  O(n)
# Space: O(h)

# iterative dfs

class Solution2(object):
    def countGoodNodes(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        def dfs(u, p):
            total = l = 0
            valid = True
            for v in adj[u]:
                if v == p:
                    continue
                cnt = dfs(v, u)
                total += cnt
                l += 1
                if l*cnt != total:
                    valid = False
            if valid:
                result[0] += 1
            return total+1
        
        adj = [[] for _ in xrange(len(edges)+1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        result = [0]
        dfs(0, -1)
        return result[0]