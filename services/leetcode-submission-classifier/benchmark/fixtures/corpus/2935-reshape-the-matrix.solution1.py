# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: reshape-the-matrix
# source_path: LeetCode-Solutions-master/Python/reshape-the-matrix.py
# solution_class: Solution
# submission_id: b40eba920b6a001a59428a8c0de0b454438e8efa
# seed: 3658795117

# Time:  O(m * n)
# Space: O(m * n)

class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if not nums or \
           r*c != len(nums) * len(nums[0]):
            return nums

        result = [[0 for _ in xrange(c)] for _ in xrange(r)]
        count = 0
        for i in xrange(len(nums)):
            for j in xrange(len(nums[0])):
                result[count/c][count%c] = nums[i][j]
                count += 1
        return result