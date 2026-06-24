# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-the-number-of-good-pairs-i
# source_path: LeetCode-Solutions-master/Python/find-the-number-of-good-pairs-i.py
# solution_class: Solution
# submission_id: ce00a4211992a22d7e38ac84d464b382d0831e2e
# seed: 3565971652

# Time:  O(rlogr + n + m)
# Space: O(r)

import collections


# number theory, freq table

class Solution(object):
    def numberOfPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: int
        """
        cnt = [0]*(max(nums1)+1)
        for x, c in collections.Counter(k*x for x in nums2).iteritems():
            for i in xrange(1, (len(cnt)-1)//x+1):
                cnt[i*x] += c
        return sum(cnt[x] for x in nums1)