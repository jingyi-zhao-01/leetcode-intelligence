# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimize-length-of-array-using-operations
# source_path: LeetCode-Solutions-master/Python/minimize-length-of-array-using-operations.py
# solution_class: Solution
# submission_id: 292624e4be4f001e0cd45b9c68e4d11376be888d
# seed: 1444987817

# Time:  O(n)
# Space: O(1)

# greedy

class Solution(object):
    def minimumArrayLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mn = min(nums)
        return (nums.count(mn)+1)//2 if all(x%mn == 0 for x in nums) else 1