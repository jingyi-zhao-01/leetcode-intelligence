# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: create-components-with-same-value
# source_path: LeetCode-Solutions-master/Python/create-components-with-same-value.py
# solution_class: Solution
# submission_id: 8fea1fc5528934f085d9278519e97179a8f7ed7a
# seed: 3591604248

# Time:  O(n * sqrt(n))
# Space: O(n)

# bfs, greedy

class Solution(object):
    def componentValue(self, nums, edges):
        """
        :type nums: List[int]
        :type edges: List[List[int]]
        :rtype: int
        """
        def bfs(target):
            total = nums[:]
            lookup = [len(adj[u]) for u in xrange(len(adj))]
            q = [u for u in xrange(len(adj)) if lookup[u] == 1]
            while q:
                new_q = []
                for u in q:
                    if total[u] > target:
                        return False
                    if total[u] == target:
                        total[u] = 0
                    for v in adj[u]:
                        total[v] += total[u]
                        lookup[v] -= 1
                        if lookup[v] == 1:
                            new_q.append(v)
                q = new_q
            return True

        result = 0
        adj = [[] for _ in xrange(len(nums))]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        total = sum(nums)
        for cnt in reversed(xrange(2, len(nums)+1)):
            if total%cnt == 0 and bfs(total//cnt):
                return cnt-1
        return 0