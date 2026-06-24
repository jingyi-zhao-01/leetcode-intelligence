# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: tree-diameter
# source_path: LeetCode-Solutions-master/Python/tree-diameter.py
# solution_class: Solution
# submission_id: 39f3d30500a8db9b0ed98638404357d5eb550605
# seed: 4158467584

# Time:  O(|V| + |E|)
# Space: O(|E|)

# iterative dfs

class Solution(object):
    def treeDiameter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        def iter_dfs():
            result = 0
            stk = [(1, (0, -1, [0]))]
            while stk:
                step, args = stk.pop()
                if step == 1:
                    u, p, ret = args
                    for v in reversed(adj[u]):
                        if v == p:
                            continue
                        ret2 = [0]
                        stk.append((2, (ret2, ret)))
                        stk.append((1, (v, u, ret2)))
                elif step == 2:
                    ret2, ret = args
                    result = max(result, ret[0]+(ret2[0]+1))
                    ret[0] = max(ret[0], ret2[0]+1)
            return result
        
        adj = [[] for _ in range(len(edges)+1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        return iter_dfs()