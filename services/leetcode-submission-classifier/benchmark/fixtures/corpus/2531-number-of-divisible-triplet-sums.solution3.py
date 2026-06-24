# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-divisible-triplet-sums
# source_path: LeetCode-Solutions-master/Python/number-of-divisible-triplet-sums.py
# solution_class: Solution3
# submission_id: 7f0ee17d58cbcdb535fe31f9715e838e57a4c413
# seed: 4267067233

# Time:  O(n^2)
# Space: O(n)

import collections


# freq table

class Solution3(object):
    def divisibleTripletCount(self, nums, d):
        """
        :type nums: List[int]
        :type d: int
        :rtype: int
        """
        result = 0
        for i in xrange(len(nums)):
            cnt = collections.Counter()
            for j in xrange(i+1, len(nums)):
                result += cnt[nums[j]%d]
                cnt[-(nums[i]+nums[j])%d] += 1
        return result