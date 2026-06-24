# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: paths-in-maze-that-lead-to-same-room
# source_path: LeetCode-Solutions-master/Python/paths-in-maze-that-lead-to-same-room.py
# solution_class: Solution
# submission_id: 7859396e0bf26e67288d7ef4a2cfb23c3616c279
# seed: 4129332429

# Time:  O(|V|^3)
# Space: O(|E|)

class Solution(object):
    def numberOfPaths(self, n, corridors):
        """
        :type n: int
        :type corridors: List[List[int]]
        :rtype: int
        """
        adj = [set() for _ in xrange(n)]
        for u, v in corridors:
            adj[min(u, v)-1].add(max(u, v)-1)
        return sum(k in adj[i] for i in xrange(n) for j in adj[i] for k in adj[j])