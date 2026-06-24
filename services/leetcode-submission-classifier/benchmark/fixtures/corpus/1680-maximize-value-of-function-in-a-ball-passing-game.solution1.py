# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximize-value-of-function-in-a-ball-passing-game
# source_path: LeetCode-Solutions-master/Python/maximize-value-of-function-in-a-ball-passing-game.py
# solution_class: Solution
# submission_id: aca7467f254f3941e44f0b3696993fa0df7745ef
# seed: 2699010683

# Time:  O(n)
# Space: O(n)

import collections


# graph, prefix sum, two pointers, sliding window

class Solution(object):
    def getMaxFunctionValue(self, receiver, k):
        """
        :type receiver: List[int]
        :type k: int
        :rtype: int
        """
        def find_cycles(adj):
            result = []
            lookup = [0]*len(adj)
            idx = 0
            for u in xrange(len(adj)):
                prev = idx
                while not lookup[u]:
                    idx += 1
                    lookup[u] = idx
                    u = adj[u]
                if lookup[u] > prev:
                    result.append((u, idx-lookup[u]+1))
            return result

        def find_prefixes():
            lookup = [(-1, -1)]*len(receiver)
            prefixes = [[0] for _ in xrange(len(cycles))]
            for idx, (u, l) in enumerate(cycles):
                for i in xrange(l):
                    lookup[u] = (idx, i)
                    prefixes[idx].append(prefixes[idx][i]+u)
                    u = receiver[u]
            return lookup, prefixes
        
        def get_sum(prefix, i, cnt):
            l = len(prefix)-1
            q, r = divmod(cnt, l)
            return (q*prefix[-1]+
                    (prefix[min(i+r, l)]-prefix[i])+
                    (prefix[max(((i+r)-l, 0))]-prefix[0]))
        
        def start_inside_cycle():
            result = 0
            for u, l in cycles:
                for _ in xrange(l):
                    idx, i = lookup[u]
                    result = max(result, get_sum(prefixes[idx], i, k+1))
                    u = receiver[u]
            return result
    
        def start_outside_cycle():
            result = 0
            degree = [0]*len(receiver)
            for x in receiver:
                degree[x] += 1
            for u in xrange(len(receiver)):
                if degree[u]:
                    continue
                curr = 0
                dq = collections.deque()
                while lookup[u][0] == -1:
                    curr += u
                    dq.append(u)
                    if len(dq) == k+1:
                        result = max(result, curr)
                        curr -= dq.popleft()
                    u = receiver[u]
                idx, i = lookup[u]
                while dq:
                    result = max(result, curr+get_sum(prefixes[idx], i, (k+1)-len(dq)))
                    curr -= dq.popleft()
            return result
            
        cycles = find_cycles(receiver)
        lookup, prefixes = find_prefixes()
        return max(start_inside_cycle(), start_outside_cycle())