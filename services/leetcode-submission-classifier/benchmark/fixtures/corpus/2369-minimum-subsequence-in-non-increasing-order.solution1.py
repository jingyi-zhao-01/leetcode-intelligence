# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-subsequence-in-non-increasing-order
# source_path: LeetCode-Solutions-master/Python/minimum-subsequence-in-non-increasing-order.py
# solution_class: Solution
# submission_id: 60a6f057c7f7eee29ec2df0e8006bae833867bba
# seed: 1113637373

# Time:  O(nlogn)
# Space: O(1)

class Solution(object):
    def minSubsequence(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result, total, curr = [], sum(nums), 0
        nums.sort(reverse=True)
        for i, x in enumerate(nums):
            curr += x
            if curr > total-curr:
                break
        return nums[:i+1]