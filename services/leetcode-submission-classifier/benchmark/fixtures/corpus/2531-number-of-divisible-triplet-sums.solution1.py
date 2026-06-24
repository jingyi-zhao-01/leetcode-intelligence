# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-divisible-triplet-sums
# source_path: LeetCode-Solutions-master/Python/number-of-divisible-triplet-sums.py
# solution_class: Solution
# submission_id: 416e187ac8dfe3a29e8d75c20708e6e5e14b50c1
# seed: 4120408185

# Time:  O(n^2)
# Space: O(n)

import collections


# freq table

class Solution(object):
    def divisibleTripletCount(self, nums, d):
        """
        :type nums: List[int]
        :type d: int
        :rtype: int
        """
        result = 0
        cnt = collections.Counter()
        for i in xrange(len(nums)):
            for j in xrange(i+1, len(nums)):
                if (nums[i]+nums[j])%d in cnt:
                    result += cnt[(nums[i]+nums[j])%d]
            cnt[-nums[i]%d] += 1
        return result