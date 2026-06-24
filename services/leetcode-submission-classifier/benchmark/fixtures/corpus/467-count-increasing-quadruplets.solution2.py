# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-increasing-quadruplets
# source_path: LeetCode-Solutions-master/Python/count-increasing-quadruplets.py
# solution_class: Solution2
# submission_id: 8ff0b8fce8266da581cdbc361b34b85f5c635932
# seed: 3325733742

# Time:  O(n^2)
# Space: O(n)

# dp

class Solution2(object):
    def countQuadruplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        right = [[0]*(len(nums)+1) for _ in xrange(len(nums))]
        for j in xrange(len(nums)):
            for i in reversed(xrange(j+1, len(nums))):
                right[j][i] = right[j][i+1] + int(nums[i] > nums[j])
        result = 0
        for k in xrange(len(nums)):
            left = 0
            for j in xrange(k):
                if nums[k] < nums[j]:
                    result += left*right[j][k+1]
                left += int(nums[k] > nums[j])
        return result