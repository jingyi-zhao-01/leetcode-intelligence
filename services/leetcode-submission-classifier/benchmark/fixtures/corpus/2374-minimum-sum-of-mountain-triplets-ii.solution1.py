# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-sum-of-mountain-triplets-ii
# source_path: LeetCode-Solutions-master/Python/minimum-sum-of-mountain-triplets-ii.py
# solution_class: Solution
# submission_id: 2cced085a892dfd278f21b5fc198e378abb3c6cf
# seed: 3268190740

# Time:  O(n)
# Space: O(n)

# prefix sum

class Solution(object):
    def minimumSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        INF = float("inf")

        right = [INF]*len(nums)
        curr = INF
        for i in reversed(xrange(len(nums))):
            right[i] = curr
            curr = min(curr, nums[i])
        result = curr = INF
        for i in xrange(len(nums)):
            if curr < nums[i] > right[i]:
                result = min(result, curr+nums[i]+right[i])
            curr = min(curr, nums[i])
        return result if result != INF else -1