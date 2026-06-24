# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximal-network-rank
# source_path: LeetCode-Solutions-master/Python/maximal-network-rank.py
# solution_class: Solution3
# submission_id: c662779f4e8ee8502d302482aff5dfabfd16887b
# seed: 948067761

# Time:  O(m + n + k^2), k is the number of values greater or equal to top2
# Space: O(m + n)

# optimized from Solution2 with counting sort

class Solution3(object):
    def maximalNetworkRank(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        degree = [0]*n
        adj = collections.defaultdict(set)
        for a, b in roads:
            degree[a] += 1
            degree[b] += 1
            adj[a].add(b)
            adj[b].add(a)
        result = 0
        for i in xrange(n-1):
            for j in xrange(i+1, n):
                result = max(result, degree[i]+degree[j]-int(i in adj and j in adj[i]))
        return result