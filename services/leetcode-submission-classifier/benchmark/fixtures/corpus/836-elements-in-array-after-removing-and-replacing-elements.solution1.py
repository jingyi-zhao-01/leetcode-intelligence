# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: elements-in-array-after-removing-and-replacing-elements
# source_path: LeetCode-Solutions-master/Python/elements-in-array-after-removing-and-replacing-elements.py
# solution_class: Solution
# submission_id: aa3a64b74375926b0e28aa6101bfdece360f6e81
# seed: 988692138

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def elementInNums(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        result = []
        for t, i in queries:
            t %= 2*len(nums)
            if t+i < len(nums):
                result.append(nums[t+i])
            elif i < t-len(nums):
                result.append(nums[i])
            else:
                result.append(-1)
        return result