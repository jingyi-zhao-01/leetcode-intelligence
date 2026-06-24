# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-number-of-distinct-elements-after-operations
# source_path: LeetCode-Solutions-master/Python/maximum-number-of-distinct-elements-after-operations.py
# solution_class: Solution
# submission_id: 049c2ee982ce1bca97f6aaf99f424e816c328e2b
# seed: 4112448257

# Time:  O(nlogn)
# Space: O(1)

# sort, greedy

class Solution(object):
    def maxDistinctElements(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        result = 0
        nums.sort()
        curr = float("-inf")
        for x in nums:
            if curr > x+k:
                continue
            curr = max(curr, x-k)+1
            result += 1
        return result