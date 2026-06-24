# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-equal-and-divisible-pairs-in-an-array
# source_path: LeetCode-Solutions-master/Python/count-equal-and-divisible-pairs-in-an-array.py
# solution_class: Solution3
# submission_id: e018de0909b0119bb227a1c8453e9451e9dd3f33
# seed: 1254107736

# Time:  O(nlogk + n * sqrt(k))
# Space: O(n + sqrt(k)), number of factors of k is at most sqrt(k)

import collections


# math, number theory

class Solution3(object):
    def countPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        idxs = collections.defaultdict(list)
        for i, x in enumerate(nums):
            idxs[x].append(i)
        return sum(idx[i]*idx[j]%k == 0 for idx in idxs.itervalues() for i in xrange(len(idx)) for j in xrange(i+1, len(idx)))