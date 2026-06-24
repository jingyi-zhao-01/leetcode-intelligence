# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-operations-to-sort-a-permutation
# source_path: LeetCode-Solutions-master/Python/minimum-operations-to-sort-a-permutation.py
# solution_class: Solution
# submission_id: 5a9c8d8152d9f48426a772609c20b269680fa3db
# seed: 3937760204

# Time:  O(n)
# Space: O(1)

# array

class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def check(i, d):
            return all(nums[(i+j*d)%len(nums)] == j for j in xrange(len(nums)))

        idx = nums.index(0)
        return min(idx, 1+(len(nums)-idx)+1) if check(idx, +1) else min((idx+1)+1, 1+(len(nums)-(idx+1))) if check(idx, -1) else -1