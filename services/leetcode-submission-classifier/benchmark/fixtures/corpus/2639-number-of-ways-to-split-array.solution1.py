# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-ways-to-split-array
# source_path: LeetCode-Solutions-master/Python/number-of-ways-to-split-array.py
# solution_class: Solution
# submission_id: 547a7b76c31134e04c0fe24841a53146b4bd2f14
# seed: 1637857064

# Time:  O(n)
# Space: O(1)

# prefix sum

class Solution(object):
    def waysToSplitArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = sum(nums)
        result = curr = 0
        for i in xrange(len(nums)-1):
            curr += nums[i]
            result += int(curr >= total-curr)
        return result