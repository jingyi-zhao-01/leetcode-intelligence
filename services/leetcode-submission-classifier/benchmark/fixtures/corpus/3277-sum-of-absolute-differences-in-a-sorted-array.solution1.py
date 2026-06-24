# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: sum-of-absolute-differences-in-a-sorted-array
# source_path: LeetCode-Solutions-master/Python/sum-of-absolute-differences-in-a-sorted-array.py
# solution_class: Solution
# submission_id: ab05eaa31f9d3f197233d6056962e88b4557bd77
# seed: 1102086298

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def getSumAbsoluteDifferences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prefix, suffix = 0, sum(nums)
        result = []
        for i, num in enumerate(nums):
            suffix -= num
            result.append((i*num-prefix) + (suffix-((len(nums)-1)-i)*num))
            prefix += num
        return result