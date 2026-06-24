# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: smallest-missing-integer-greater-than-sequential-prefix-sum
# source_path: LeetCode-Solutions-master/Python/smallest-missing-integer-greater-than-sequential-prefix-sum.py
# solution_class: Solution
# submission_id: 69e7c337d70d2c5dbac38017b6bd338bf5ac8580
# seed: 3897173758

# Time:  O(n)
# Space: O(n)

# hash table

class Solution(object):
    def missingInteger(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = nums[0]
        for i in xrange(1, len(nums)):
            if nums[i] != nums[i-1]+1:
                break
            total += nums[i]
        lookup = set(nums)
        while total in lookup:
            total += 1
        return total