# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: intersection-of-multiple-arrays
# source_path: LeetCode-Solutions-master/Python/intersection-of-multiple-arrays.py
# solution_class: Solution3
# submission_id: 7030b21f1661e0fd71543a161ae5216fb706ce21
# seed: 3176356739

# Time:  O(n * l + r), n = len(nums), l = len(nums[0])
# Space: O(r), r = max(nums)-min(nums)

# freq table, counting sort

class Solution3(object):
    def intersection(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        result = set(nums[0])
        for i in xrange(1, len(nums)):
            result = set(x for x in nums[i] if x in result)
        return sorted(result)