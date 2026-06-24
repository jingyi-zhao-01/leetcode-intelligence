# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-hamming-distances
# source_path: LeetCode-Solutions-master/Python/maximum-hamming-distances.py
# solution_class: Solution2
# submission_id: 383596b5d44fb30fa3f49470e96d90e128990505
# seed: 3757058960

# Time:  O(m * 2^m)
# Space: O(2^m)

# bitmasks, knapsack dp

class Solution2(object):
    def maxHammingDistances(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: List[int]
        """
        q = []
        dist = [-1]*(1<<m)
        for x in nums:
            if dist[x] != -1:
                continue
            dist[x] = 0
            q.append(x)
        d = 0
        while q:
            d += 1
            new_q = []
            for u in q:
                for i in xrange(m):
                    if dist[u^(1<<i)] != -1:
                        continue
                    dist[u^(1<<i)] = d
                    new_q.append(u^(1<<i))
            q = new_q
        return [m-dist[((1<<m)-1)^x] for x in nums]