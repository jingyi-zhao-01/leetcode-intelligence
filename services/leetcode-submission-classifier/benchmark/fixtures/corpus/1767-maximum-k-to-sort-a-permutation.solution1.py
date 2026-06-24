# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-k-to-sort-a-permutation
# source_path: LeetCode-Solutions-master/Python/maximum-k-to-sort-a-permutation.py
# solution_class: Solution
# submission_id: e05834796a3eabc525c1a8f0345e42612da86b6e
# seed: 2967298045

# Time:  O(n)
# Space: O(1)

# sort, bitmasks, constructive algorithms

class Solution(object):
    def sortPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = -1
        for i in xrange(len(nums)):
            if nums[i] == i:
                continue
            result = result&i if result != -1 else i
        return result if result != -1 else 0