# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: sum-of-digit-differences-of-all-pairs
# source_path: LeetCode-Solutions-master/Python/sum-of-digit-differences-of-all-pairs.py
# solution_class: Solution
# submission_id: 576f2ead86dcd1bce4221d14c821e1832204d95c
# seed: 4156682147

# Time:  O(nlogr)
# Space: O(10 * logr)

# prefix sum

class Solution(object):
    def sumDigitDifferences(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        base, l = 1, 0
        while base <= nums[0]:
            base *= 10
            l += 1
        cnts = [[0]*10 for _ in xrange(l)]
        for x in nums:
            for i in xrange(l):
                cnts[i][x%10] += 1
                x //= 10
        return sum(c*(len(nums)-c) for cnt in cnts for c in cnt)//2