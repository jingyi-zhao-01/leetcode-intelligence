# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-product-of-first-and-last-elements-of-a-subsequence
# source_path: LeetCode-Solutions-master/Python/maximum-product-of-first-and-last-elements-of-a-subsequence.py
# solution_class: Solution
# submission_id: fd5d2ae87ee53b167302d9c1cd3ecde61fa3ed26
# seed: 87535814

# Time:  O(n)
# Space: O(1)

# two pointers, sliding window

class Solution(object):
    def maximumProduct(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        result = mx = float("-inf")
        mn = float("inf")
        for i in xrange(len(nums)-(m-1)):
            mx = max(mx, nums[i])
            mn = min(mn, nums[i])
            result = max(result, nums[i+(m-1)]*mx, nums[i+(m-1)]*mn)
        return result