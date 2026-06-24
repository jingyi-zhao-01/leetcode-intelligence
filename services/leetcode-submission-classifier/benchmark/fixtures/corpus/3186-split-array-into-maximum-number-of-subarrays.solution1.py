# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: split-array-into-maximum-number-of-subarrays
# source_path: LeetCode-Solutions-master/Python/split-array-into-maximum-number-of-subarrays.py
# solution_class: Solution
# submission_id: f818a676a265a1626fc7a7c7c6625bffb5cccbc0
# seed: 1386648755

# Time:  O(n)
# Space: O(1)

# greedy

class Solution(object):
    def maxSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = curr = 0
        for x in nums:
            curr = curr&x if curr else x
            if not curr:
                result += 1
        return max(result, 1)