# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: intersection-of-multiple-arrays
# source_path: LeetCode-Solutions-master/Python/intersection-of-multiple-arrays.py
# solution_class: Solution2
# submission_id: dbe584ecca1667ed6c661cbe2d4f0d7f5ebeb862
# seed: 996351320

# Time:  O(n * l + r), n = len(nums), l = len(nums[0])
# Space: O(r), r = max(nums)-min(nums)

# freq table, counting sort

class Solution2(object):
    def intersection(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        result = set(nums[0])
        for i in xrange(1, len(nums)):
            result = set(x for x in nums[i] if x in result)
        return [i for i in xrange(min(result), max(result)+1) if i in result] if result else []