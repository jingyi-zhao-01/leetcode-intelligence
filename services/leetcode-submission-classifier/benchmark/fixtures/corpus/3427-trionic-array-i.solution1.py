# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: trionic-array-i
# source_path: LeetCode-Solutions-master/Python/trionic-array-i.py
# solution_class: Solution
# submission_id: ea6ab28f1e481824afc63f7bda9a9f1f5a5ec65e
# seed: 1357942398

# Time:  O(n)
# Space: O(1)

# array

class Solution(object):
    def isTrionic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        p = 0
        while p+1 < len(nums) and nums[p] < nums[p+1]:
            p += 1
        q = p
        while q+1 < len(nums) and nums[q] > nums[q+1]:
            q += 1
        i = q
        while i+1 < len(nums) and nums[i] < nums[i+1]:
            i += 1
        return 0 < p < q < i == len(nums)-1