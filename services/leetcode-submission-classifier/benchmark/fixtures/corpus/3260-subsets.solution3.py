# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: subsets
# source_path: LeetCode-Solutions-master/Python/subsets.py
# solution_class: Solution3
# submission_id: 38c75d60ffbdd1f0ecc9ce2eec5d3ac2a7d4b956
# seed: 3455955941

# Time:  O(n * 2^n)
# Space: O(1)

class Solution3(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return self.subsetsRecu([], sorted(nums))

    def subsetsRecu(self, cur, nums):
        if not nums:
            return [cur]

        return self.subsetsRecu(cur, nums[1:]) + self.subsetsRecu(cur + [nums[0]], nums[1:])