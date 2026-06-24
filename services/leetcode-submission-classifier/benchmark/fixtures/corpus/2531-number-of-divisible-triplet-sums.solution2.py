# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-divisible-triplet-sums
# source_path: LeetCode-Solutions-master/Python/number-of-divisible-triplet-sums.py
# solution_class: Solution2
# submission_id: 1be684f055067c1d259a8696891148781a429ecb
# seed: 122969886

# Time:  O(n^2)
# Space: O(n)

import collections


# freq table

class Solution2(object):
    def divisibleTripletCount(self, nums, d):
        """
        :type nums: List[int]
        :type d: int
        :rtype: int
        """
        result = 0
        cnt = collections.Counter()
        for i in xrange(len(nums)):
            if nums[i]%d in cnt:
                result += cnt[nums[i]%d]
            for j in xrange(i):
                cnt[-(nums[i]+nums[j])%d] += 1
        return result