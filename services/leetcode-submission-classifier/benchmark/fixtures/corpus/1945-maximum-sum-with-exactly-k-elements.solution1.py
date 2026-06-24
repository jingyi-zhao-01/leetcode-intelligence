# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-sum-with-exactly-k-elements
# source_path: LeetCode-Solutions-master/Python/maximum-sum-with-exactly-k-elements.py
# solution_class: Solution
# submission_id: 11602e471b87f96385faa126d2e35f1f28505774
# seed: 2670745180

# Time:  O(n)
# Space: O(1)

# math

class Solution(object):
    def maximizeSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return max(nums)*k+k*(k-1)//2