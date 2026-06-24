# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-difference-between-increasing-elements
# source_path: LeetCode-Solutions-master/Python/maximum-difference-between-increasing-elements.py
# solution_class: Solution
# submission_id: 229b6a467930e7e500f50c7e2db9ed46a801a30d
# seed: 10269784

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def maximumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result, prefix = 0, float("inf")
        for x in nums: 
            result = max(result, x-prefix)
            prefix = min(prefix, x)
        return result if result else -1