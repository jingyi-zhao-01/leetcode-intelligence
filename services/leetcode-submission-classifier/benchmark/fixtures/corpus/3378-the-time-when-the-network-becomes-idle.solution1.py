# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: the-time-when-the-network-becomes-idle
# source_path: LeetCode-Solutions-master/Python/the-time-when-the-network-becomes-idle.py
# solution_class: Solution
# submission_id: 440e6f8f1664b1a3b1eb1be636f0e3117fba0d4b
# seed: 975964899

# Time:  O(|V| + |E|) = O(|E|) since graph is connected, O(|E|) >= O(|V|) 
# Space: O(|V| + |E|) = O(|E|)

class Solution(object):
    def networkBecomesIdle(self, edges, patience):
        """
        :type edges: List[List[int]]
        :type patience: List[int]
        :rtype: int
        """
        adj = [[] for _ in xrange(len(patience))]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        q = [0]
        lookup = [False]*len(patience)
        lookup[0] = True
        step = 1
        result = 0
        while q:
            new_q = []
            for u in q:
                for v in adj[u]:
                    if lookup[v]:
                        continue
                    lookup[v] = True
                    new_q.append(v)
                    result = max(result, ((step*2)-1)//patience[v]*patience[v] + (step*2))
            q = new_q
            step += 1
        return 1+result