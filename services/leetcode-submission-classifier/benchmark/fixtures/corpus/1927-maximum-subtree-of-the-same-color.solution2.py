# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-subtree-of-the-same-color
# source_path: LeetCode-Solutions-master/Python/maximum-subtree-of-the-same-color.py
# solution_class: Solution2
# submission_id: d0cf8a9dcec8976f1a9aaa993699cb0c061d6ef5
# seed: 966736459

# Time:  O(n)
# Space: O(h)

# iterative dfs

class Solution2(object):
    def maximumSubtreeSize(self, edges, colors):
        """
        :type edges: List[List[int]]
        :type colors: List[int]
        :rtype: int
        """
        def dfs(u, p):
            cnt = 1
            for v in adj[u]:
                if v == p:
                    continue
                c = dfs(v, u)
                if cnt == -1:
                    continue
                if c == -1 or colors[v] != colors[u]:
                    cnt = -1
                    continue
                cnt += c
            result[0] = max(result[0], cnt)
            return cnt

        adj = [[] for _ in xrange(len(colors))]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        result = [0]
        dfs(0, -1)
        return result[0]