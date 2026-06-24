# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-almost-equal-pairs-ii
# source_path: LeetCode-Solutions-master/Python/count-almost-equal-pairs-ii.py
# solution_class: Solution2
# submission_id: 553f8417e00f4c81e0d1da722fa44776ff0b899a
# seed: 2024907624

# Time:  O(n * l^4)
# Space: O(n * l^2 + min(n * l^4, n^2)) = O(n * l^4)

import collections


# freq table, combinatorics

class Solution2(object):
    def countPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        L = 7
        K = 2
        POW10 = [0]*L
        POW10[0] = 1
        for i in xrange(L-1):
            POW10[i+1] = POW10[i]*10
        def at_most(k, x):
            lookup = {x}
            result = [x]
            u = 0
            for _ in xrange(k):
                for u in xrange(u, len(result)):
                    x = result[u]
                    for i in xrange(L):
                        a = x//POW10[i]%10
                        for j in xrange(i+1, L):
                            b = x//POW10[j]%10
                            if a == b:
                                continue
                            y = x-a*(POW10[i]-POW10[j])+b*(POW10[i]-POW10[j])
                            if y in lookup:
                                continue
                            lookup.add(y)
                            result.append(y)
            return result

        result = 0
        cnt1 = collections.Counter(nums)
        cnt2 = collections.Counter()
        for x, v in cnt1.iteritems():
            result += cnt2[x]*v+v*(v-1)//2
            for x in at_most(K, x):
                if x not in cnt1:
                    continue
                cnt2[x] += v
        return result