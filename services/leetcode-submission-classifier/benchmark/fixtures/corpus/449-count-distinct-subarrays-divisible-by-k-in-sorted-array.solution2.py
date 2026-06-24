# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-distinct-subarrays-divisible-by-k-in-sorted-array
# source_path: LeetCode-Solutions-master/Python/count-distinct-subarrays-divisible-by-k-in-sorted-array.py
# solution_class: Solution2
# submission_id: 3e58ea087b63ea3d3cad7e2e1e6b63828cd1a48e
# seed: 2584117447

# Time:  O(n)
# Space: O(min(n, k))

import collections


# prefix sum, freq table

class Solution2(object):
    def numGoodSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        result = prefix = 0
        cnt = collections.defaultdict(int)
        cnt[0] = 1
        for x in nums:
            prefix = (prefix+x)%k
            result += cnt[prefix]
            cnt[prefix] += 1
        l = 0
        for i in xrange(len(nums)):
            l += 1
            if i+1 == len(nums) or nums[i+1] != nums[i]:
                for j in xrange(1, l+1):
                    if nums[i]*j%k == 0:
                        result -= (l-j+1)-1
                l = 0
        return result