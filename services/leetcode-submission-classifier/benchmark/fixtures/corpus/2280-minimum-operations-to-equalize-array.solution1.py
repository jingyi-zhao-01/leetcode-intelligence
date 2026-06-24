# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-operations-to-equalize-array
# source_path: LeetCode-Solutions-master/Python/minimum-operations-to-equalize-array.py
# solution_class: Solution
# submission_id: d9841945c70ac09f0986809165a37ab11825ca69
# seed: 3278588970

# Time:  O(n)
# Space: O(1)

# array

class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return 0 if all(x == nums[0] for x in nums) else 1