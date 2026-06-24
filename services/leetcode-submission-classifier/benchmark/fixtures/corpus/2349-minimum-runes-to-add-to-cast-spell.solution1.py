# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-runes-to-add-to-cast-spell
# source_path: LeetCode-Solutions-master/Python/minimum-runes-to-add-to-cast-spell.py
# solution_class: Solution
# submission_id: 2c6ca853e01e38b2f4a4676f33af675fc5678c85
# seed: 3127224959

# Time:  O(n)
# Space: O(n)

# tarjan's algorithm, SCC, strongly connected compoenents
# reference: https://en.wikipedia.org/wiki/Tarjan%27s_strongly_connected_components_algorithm
def strongly_connected_components(adj):  # Time: O(|V| + |E|) = O(N + 2N) = O(N), Space: O(|V|) = O(N)
    def strongconnect(v):
        index[v] = index_counter[0]
        lowlinks[v] = index_counter[0]
        index_counter[0] += 1
        stack_set[v] = True
        stack.append(v)
        for w in adj[v]:
            if index[w] == -1:
                strongconnect(w)
                lowlinks[v] = min(lowlinks[v], lowlinks[w])
            elif stack_set[w]:
                lowlinks[v] = min(lowlinks[v], index[w])
        if lowlinks[v] == index[v]:
            connected_component = []
            w = None
            while w != v:
                w = stack.pop()
                stack_set[w] = False
                connected_component.append(w)
            result.append(connected_component)

    index_counter, index, lowlinks = [0], [-1]*len(adj), [-1]*len(adj)
    stack, stack_set = [], [False]*len(adj)
    result = []
    for v in xrange(len(adj)):
        if index[v] == -1:
            strongconnect(v)
    return result

class Solution(object):
    def minRunesToAdd(self, n, crystals, flowFrom, flowTo):
        """
        :type n: int
        :type crystals: List[int]
        :type flowFrom: List[int]
        :type flowTo: List[int]
        :rtype: int
        """
        adj = [[] for _ in xrange(n)]
        for i in xrange(len(flowFrom)):
            adj[flowFrom[i]].append(flowTo[i])
        lookup = [-1]*n
        sccs = strongly_connected_components(adj)
        for i, scc in enumerate(sccs):
            for x in scc:
                lookup[x] = i
        result = [False]*len(sccs)
        for u in xrange(n):
            for v in adj[u]:
                if lookup[v] != lookup[u]:
                    result[lookup[v]] = True
        for x in crystals:
            result[lookup[x]] = True
        return sum(not x for x in result)