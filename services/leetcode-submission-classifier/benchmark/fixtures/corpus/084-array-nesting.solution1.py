# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: array-nesting
# source_path: LeetCode-Solutions-master/Python/array-nesting.py
# solution_class: Solution
# submission_id: d149949b957b777b1acb4bf53e16f3e50a687aea
# seed: 1185602582

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for num in nums:
            if num is not None:
                start, count = num, 0
                while nums[start] is not None:
                    temp = start
                    start = nums[start]
                    nums[temp] = None
                    count += 1
                result = max(result, count)
        return result