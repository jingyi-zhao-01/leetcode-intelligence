# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: k-divisible-elements-subarrays
# source_path: LeetCode-Solutions-master/Python/k-divisible-elements-subarrays.py
# solution_class: Solution3
# submission_id: 411b6c1c0b3a262ce6b043da21484a6c08a2957a
# seed: 95076046

# Time:  O(n^2)
# Space: O(t), t is the size of trie

import collections


# trie

class Solution3(object):
    def countDistinct(self, nums, k, p):
        """
        :type nums: List[int]
        :type k: int
        :type p: int
        :rtype: int
        """
        MOD, P = 10**9+7, 200
        result = 0
        cnt, h = [0]*len(nums), [0]*len(nums)
        for l in xrange(1, len(nums)+1):
            lookup = set()
            for i in xrange(len(nums)-l+1):
                cnt[i] += (nums[i+l-1]%p == 0)
                if cnt[i] > k:
                    continue
                h[i] = (h[i]*P+nums[i+l-1])%MOD
                lookup.add(h[i])
            result += len(lookup)
        return result