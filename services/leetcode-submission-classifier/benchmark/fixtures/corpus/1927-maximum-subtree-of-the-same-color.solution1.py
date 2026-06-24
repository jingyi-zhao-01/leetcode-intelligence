# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-subtree-of-the-same-color
# source_path: LeetCode-Solutions-master/Python/maximum-subtree-of-the-same-color.py
# solution_class: Solution
# submission_id: d2f0336890ca06d3af27d0397c4cf4a2f4bb3c1f
# seed: 513300093

# Time:  O(n)
# Space: O(h)

# iterative dfs

class Solution(object):
    def maximumSubtreeSize(self, edges, colors):
        """
        :type edges: List[List[int]]
        :type colors: List[int]
        :rtype: int
        """
        def iter_dfs():
            result = 0
            stk = [(1, (0, -1, [1]))]
            while stk:
                step, args = stk.pop()
                if step == 1:
                    u, p, ret = args
                    stk.append((4, (ret,)))
                    stk.append((2, (u, p, ret, 0)))
                elif step == 2:
                    u, p, ret, i = args
                    if i == len(adj[u]):
                        continue
                    v = adj[u][i]
                    stk.append((2, (u, p, ret, i+1)))
                    if v == p:
                        continue
                    new_ret = [1]
                    stk.append((3, (v, u, new_ret, ret)))
                    stk.append((1, (v, u, new_ret)))
                elif step == 3:
                    v, u, new_ret, ret = args
                    if ret[0] == -1:
                        continue 
                    if new_ret[0] == 0 or colors[v] != colors[u]:
                        ret[0] = -1
                        continue
                    ret[0] += new_ret[0]
                elif step == 4:
                    ret = args[0]
                    result = max(result, ret[0])
            return result

        adj = [[] for _ in xrange(len(colors))]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        return iter_dfs()