# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: make-sum-divisible-by-p
# source_path: LeetCode-Solutions-master/Python/make-sum-divisible-by-p.py
# solution_class: Solution
# submission_id: ef37304de58149cd602f608db288096d4cfddc42
# seed: 5583513

# Time:  O(n)
# Space: O(p)

class Solution(object):
    def minSubarray(self, nums, p):
        """
        :type nums: List[int]
        :type p: int
        :rtype: int
        """
        residue = sum(nums) % p
        if not residue:
            return 0
        result = len(nums)
        curr, lookup = 0, {0: -1}
        for i, num in enumerate(nums):
            curr = (curr+num) % p
            lookup[curr] = i
            if (curr-residue) % p in lookup:
                result = min(result, i-lookup[(curr-residue)%p])
        return result if result < len(nums) else -1