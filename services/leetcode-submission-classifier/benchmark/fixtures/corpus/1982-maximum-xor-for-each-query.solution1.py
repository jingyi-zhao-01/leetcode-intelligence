# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-xor-for-each-query
# source_path: LeetCode-Solutions-master/Python/maximum-xor-for-each-query.py
# solution_class: Solution
# submission_id: 0c76699761ee1e506acd5acbb65ad619d1b3da22
# seed: 185112661

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def getMaximumXor(self, nums, maximumBit):
        """
        :type nums: List[int]
        :type maximumBit: int
        :rtype: List[int]
        """
        result = [0]*len(nums)
        mask = 2**maximumBit-1
        for i in xrange(len(nums)):
            mask ^= nums[i]
            result[-1-i] = mask
        return result