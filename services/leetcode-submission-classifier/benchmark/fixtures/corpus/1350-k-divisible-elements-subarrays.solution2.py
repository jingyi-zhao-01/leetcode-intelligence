# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: k-divisible-elements-subarrays
# source_path: LeetCode-Solutions-master/Python/k-divisible-elements-subarrays.py
# solution_class: Solution2
# submission_id: 76acd41096aee5d7e1bdf03bd0daca30107c0f96
# seed: 3683210788

# Time:  O(n^2)
# Space: O(t), t is the size of trie

import collections


# trie

class Solution2(object):
    def countDistinct(self, nums, k, p):
        """
        :type nums: List[int]
        :type k: int
        :type p: int
        :rtype: int
        """
        MOD, P = 10**9+7, 113
        def check(nums, lookup, l, i):
            return all(any(nums[i+k] != nums[j+k] for k in xrange(l)) for j in lookup)

        result = 0
        cnt, h = [0]*len(nums), [0]*len(nums)
        for l in xrange(1, len(nums)+1):
            lookup = collections.defaultdict(list)
            for i in xrange(len(nums)-l+1):
                cnt[i] += (nums[i+l-1]%p == 0)
                if cnt[i] > k:
                    continue
                h[i] = (h[i]*P+nums[i+l-1])%MOD
                if not check(nums, lookup[h[i]], l, i):
                    continue
                lookup[h[i]].append(i)
                result += 1
        return result