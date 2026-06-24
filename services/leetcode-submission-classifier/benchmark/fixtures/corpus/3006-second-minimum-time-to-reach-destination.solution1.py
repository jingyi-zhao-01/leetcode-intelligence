# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: second-minimum-time-to-reach-destination
# source_path: LeetCode-Solutions-master/Python/second-minimum-time-to-reach-destination.py
# solution_class: Solution
# submission_id: fc4df4f4e5c7b611b906f04b3a6522625dca5802
# seed: 2453303220

# Time:  O(|V| + |E|) = O(|E|) since graph is connected, O(|E|) >= O(|V|) 
# Space: O(|V| + |E|) = O(|E|)

class Solution(object):
    def secondMinimum(self, n, edges, time, change):
        """
        :type n: int
        :type edges: List[List[int]]
        :type time: int
        :type change: int
        :rtype: int
        """
        # Template:
        # https://github.com/kamyu104/LeetCode-Solutions/blob/master/Python/find-if-path-exists-in-graph.py
        def bi_bfs(adj, start, target):
            left, right = {start}, {target}
            lookup = set()
            result = steps = 0
            while left and (not result or result+2 > steps):  # modified
                for u in left:
                    lookup.add(u)
                new_left = set()
                for u in left: 
                    if u in right:
                        if not result:  # modified
                            result = steps
                        elif result < steps:  # modifeid
                            return result+1
                    for v in adj[u]:
                        if v in lookup:
                            continue
                        new_left.add(v)
                left = new_left
                steps += 1
                if len(left) > len(right): 
                    left, right = right, left
            return result+2  # modified

        def calc_time(time, change, dist):
            result = 0
            for _ in xrange(dist):
                if result//change%2:
                    result = (result//change+1)*change
                result += time
            return result

        adj = [[] for _ in xrange(n)]
        for u, v in edges:
            adj[u-1].append(v-1)
            adj[v-1].append(u-1)
        return calc_time(time, change, bi_bfs(adj, 0, n-1))