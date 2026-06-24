# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: semi-ordered-permutation
# source_path: LeetCode-Solutions-master/Python/semi-ordered-permutation.py
# solution_class: Solution
# submission_id: 43c5be8406680639d97428a44911e548e15ab52f
# seed: 3461156116

# Time:  O(n)
# Space: O(1)

# greedy

class Solution(object):
    def semiOrderedPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i, j = nums.index(1), nums.index(len(nums))
        return i+((len(nums)-1)-j)-int(i > j)