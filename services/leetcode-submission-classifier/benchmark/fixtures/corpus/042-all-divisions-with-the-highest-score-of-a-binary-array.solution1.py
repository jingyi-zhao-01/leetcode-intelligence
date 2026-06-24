# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: all-divisions-with-the-highest-score-of-a-binary-array
# source_path: LeetCode-Solutions-master/Python/all-divisions-with-the-highest-score-of-a-binary-array.py
# solution_class: Solution
# submission_id: 07391304dd1d6ac376cbd6c1fbff2065f5dfe4f1
# seed: 3623228584

# Time:  O(n)
# Space: O(1)

# prefix sum

class Solution(object):
    def maxScoreIndices(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        mx = zeros = 0
        total = sum(nums)
        for i in xrange(len(nums)+1):
            zeros += ((nums[i-1] if i else 0) == 0)
            if zeros+(total-(i-zeros)) > mx:
                mx = zeros+(total-(i-zeros))
                result = []
            if zeros+(total-(i-zeros)) == mx:
                result.append(i)
        return result