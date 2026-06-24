# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-cost-to-make-array-equalindromic
# source_path: LeetCode-Solutions-master/Python/minimum-cost-to-make-array-equalindromic.py
# solution_class: Solution2
# submission_id: b57a86a7a9cc365ea17ca6550c7bb6c481e032f1
# seed: 2530664440

# Time:  O(n + logr)
# Space: O(logr)

import random


# lc0564
# quick select, math, string

class Solution2(object):
    def minimumCost(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def nearest_palindromic(x):
            n = str(x)
            l = len(n)
            result = {10**l+1, 10**(l-1)-1}
            prefix = int(n[:(l+1)/2])
            for i in map(str, (prefix-1, prefix, prefix+1)):
                result.add(int(i+[i, i[:-1]][l%2][::-1]))
            return result
    
        nums.sort()
        median = nums[len(nums)//2]
        if len(nums)%2 == 0:
            median = (median+nums[len(nums)//2-1])//2
        return min(sum(abs(x-p) for x in nums) for p in nearest_palindromic(median))