# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-almost-equal-pairs-ii
# source_path: LeetCode-Solutions-master/Python/count-almost-equal-pairs-ii.py
# solution_class: Solution
# submission_id: 3bc13664cfe27c0a43e79a56fbc536da4c2d29bc
# seed: 1615528033

# Time:  O(n * l^4)
# Space: O(n * l^2 + min(n * l^4, n^2)) = O(n * l^4)

import collections


# freq table, combinatorics

class Solution(object):
    def countPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        L = 7
        POW10 = [0]*L
        POW10[0] = 1
        for i in xrange(L-1):
            POW10[i+1] = POW10[i]*10
        cnt1 = collections.Counter(nums)
        adj = collections.defaultdict(list)
        cnt = list(cnt1.iteritems())
        for idx in xrange(len(cnt)):
            adj[cnt[idx][0]].append(idx)
            for i in xrange(L):
                a = cnt[idx][0]//POW10[i]%10
                for j in xrange(i+1, L):
                    b = cnt[idx][0]//POW10[j]%10
                    if a == b:
                        continue
                    adj[cnt[idx][0]-a*(POW10[i]-POW10[j])+b*(POW10[i]-POW10[j])].append(idx)
        result = sum(v*(v-1)//2 for v in cnt1.itervalues())
        lookup = set()
        for u in adj.iterkeys():
            for i in xrange(len(adj[u])):
                v1 = cnt[adj[u][i]][1]
                for j in xrange(i+1, len(adj[u])):
                    v2 = cnt[adj[u][j]][1]
                    if (adj[u][i], adj[u][j]) in lookup:
                        continue
                    lookup.add((adj[u][i], adj[u][j]))
                    result += v1*v2
        return result