# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-beautiful-splits-in-an-array
# source_path: LeetCode-Solutions-master/Python/count-beautiful-splits-in-an-array.py
# solution_class: Solution2
# submission_id: 5d783f68a5a12b7b4c03ec81d7e4394f00952d3a
# seed: 2863657102

# Time:  O(n^2)
# Space: O(n)

# z-function

class Solution2(object):
    def beautifulSplits(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [[0]*len(nums) for _ in xrange(len(nums))]
        for i in reversed(xrange(len(nums))):
            for j in xrange(i+1, len(dp)):
                dp[i][j] = 1+(dp[i+1][j+1] if j+1 < len(nums) else 0) if nums[i] == nums[j] else 0
        result = 0
        for i in xrange(1, len(nums)-1):
            for j in xrange(i+1, len(nums)):
                if (dp[0][i] >= i and j-i >= i) or dp[i][j] >= j-i:
                    result += 1
        return result