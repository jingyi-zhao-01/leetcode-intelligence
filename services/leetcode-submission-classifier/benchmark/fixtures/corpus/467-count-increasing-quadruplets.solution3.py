# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-increasing-quadruplets
# source_path: LeetCode-Solutions-master/Python/count-increasing-quadruplets.py
# solution_class: Solution3
# submission_id: 74fcba11d77933b89892c7fb230111e96e914385
# seed: 2495038505

# Time:  O(n^2)
# Space: O(n)

# dp

class Solution3(object):
    def countQuadruplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = [[0]*(len(nums)+1) for _ in xrange(len(nums))]
        for j in xrange(len(nums)):
            for i in xrange(j):
                left[j][i+1] = left[j][i] + int(nums[i] < nums[j])
        right = [[0]*(len(nums)+1) for _ in xrange(len(nums))]
        for j in xrange(len(nums)):
            for i in reversed(xrange(j+1, len(nums))):
                right[j][i] = right[j][i+1] + int(nums[i] > nums[j])
        result = 0
        for k in xrange(len(nums)):
            for j in xrange(k):
                if nums[k] < nums[j]:
                    result += left[k][j]*right[j][k+1]
        return result