# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-element-sum-of-a-complete-subset-of-indices
# source_path: LeetCode-Solutions-master/Python/maximum-element-sum-of-a-complete-subset-of-indices.py
# solution_class: Solution
# submission_id: 4cbd84fddf79f0d7fa6cfedc3ea1571f94cc7674
# seed: 2372121798

# Time:  O(n * (1 + 1/4 + 1/9 + ... + 1/x^2)) = O(pi^2 / 6 * n) = O(n), see https://en.wikipedia.org/wiki/Basel_problem
# Space: O(1)

# number theory, basel problem

class Solution(object):
    def maximumSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return max(sum(nums[i*x**2-1] for x in xrange(1, int((len(nums)//i)**0.5)+1)) for i in xrange(1, len(nums)+1))