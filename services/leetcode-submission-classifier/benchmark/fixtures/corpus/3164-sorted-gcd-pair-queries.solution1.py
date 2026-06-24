# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: sorted-gcd-pair-queries
# source_path: LeetCode-Solutions-master/Python/sorted-gcd-pair-queries.py
# solution_class: Solution
# submission_id: 739704a0768375b76e231950dd6960a8cd40a3aa
# seed: 3824669264

# Time:  O(rlogr + qlogr), r = max(nums)
# Space: O(r)

import collections
import bisect


# number theory, freq table, prefix sum, binary search

class Solution(object):
    def gcdValues(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[int]
        :rtype: List[int]
        """
        cnt1 = collections.Counter(nums)
        cnt2 = [0]*(max(nums)+1)
        for g in reversed(xrange(1, len(cnt2))):
            c = sum(cnt1[ng] for ng in xrange(g, len(cnt2), g))
            cnt2[g] = c*(c-1)//2-sum(cnt2[ng] for ng in xrange(g+g, len(cnt2), g))
        prefix = [0]*(len(cnt2)+1)
        for i in xrange(len(prefix)-1):
            prefix[i+1] = prefix[i]+cnt2[i]
        return [bisect.bisect_right(prefix, q)-1 for q in queries]