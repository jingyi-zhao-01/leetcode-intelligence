# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-the-number-of-good-nodes
# source_path: LeetCode-Solutions-master/Python/count-the-number-of-good-nodes.py
# solution_class: Solution
# submission_id: deac6a25ff5785f326bf776aa49230e5310e2f7f
# seed: 3777023652

# Time:  O(n)
# Space: O(h)

# iterative dfs

class Solution(object):
    def countGoodNodes(self, edges):
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
                    l, valid = [0], [True]
                    stk.append((4, (ret, valid)))
                    stk.append((2, (u, p, 0, ret, l, valid)))
                elif step == 2:
                    u, p, i, ret, l, valid = args
                    if i == len(adj[u]):
                        continue
                    stk.append((2, (u, p, i+1, ret, l, valid)))
                    v = adj[u][i]
                    if v == p:
                        continue
                    new_ret = [0]
                    stk.append((3, (new_ret, ret, l, valid)))
                    stk.append((1, (v, u, new_ret)))
                elif step == 3:
                    new_ret, ret, l, valid = args
                    ret[0] += new_ret[0]
                    l[0] += 1
                    if new_ret[0]*l[0] != ret[0]:
                        valid[0] = False
                elif step == 4:
                    ret, valid = args
                    if valid[0]:
                        result += 1
                    ret[0] += 1
            return result

        adj = [[] for _ in xrange(len(edges)+1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        return iter_dfs()