# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-operations-to-sort-a-permutation
# source_path: LeetCode-Solutions-master/Python/minimum-operations-to-sort-a-permutation.py
# solution_class: Solution2
# submission_id: 4e81b011d13c666ca8e66590e1155f55c209da88
# seed: 534428808

# Time:  O(n)
# Space: O(1)

# array

class Solution2(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def check(compare):
            return sum(not compare(nums[i], nums[(i+1)%len(nums)]) for i in xrange(len(nums))) <= 1

        idx = nums.index(0)
        return min(idx, 1+(len(nums)-idx)+1) if check(lambda a, b: a <= b) else min((idx+1)+1, 1+(len(nums)-(idx+1))) if check(lambda a, b: a >= b) else -1