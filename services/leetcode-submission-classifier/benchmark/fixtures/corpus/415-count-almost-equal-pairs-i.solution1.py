# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-almost-equal-pairs-i
# source_path: LeetCode-Solutions-master/Python/count-almost-equal-pairs-i.py
# solution_class: Solution
# submission_id: 36cba902cb113963daa898652b4a6e122271bddc
# seed: 3893776284

# Time:  O(n * l^2)
# Space: O(n)

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
        cnt2 = collections.Counter()
        for x, v in cnt1.iteritems():
            for i in xrange(L):
                a = x//POW10[i]%10
                for j in xrange(i+1, L):
                    b = x//POW10[j]%10
                    if a == b or x-a*(POW10[i]-POW10[j])+b*(POW10[i]-POW10[j]) not in cnt1:
                        continue
                    cnt2[x-a*(POW10[i]-POW10[j])+b*(POW10[i]-POW10[j])] += v
        return sum(v*(v-1)//2 for v in cnt1.itervalues())+sum(v*cnt2[x] for x, v in cnt1.iteritems())//2