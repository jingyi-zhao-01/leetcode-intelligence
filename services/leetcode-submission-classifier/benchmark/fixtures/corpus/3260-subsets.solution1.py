# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: subsets
# source_path: LeetCode-Solutions-master/Python/subsets.py
# solution_class: Solution
# submission_id: 5dcdc1b54d8784c7480f755429532925811f7b12
# seed: 235834665

# Time:  O(n * 2^n)
# Space: O(1)

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = [[]]
        for i in xrange(len(nums)):
            size = len(result)
            for j in xrange(size):
                result.append(list(result[j]))
                result[-1].append(nums[i])
        return result