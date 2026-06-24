# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: zero-array-transformation-iv
# source_path: LeetCode-Solutions-master/Python/zero-array-transformation-iv.py
# solution_class: Solution2
# submission_id: 262bac7e84555e0f854ad69b1bdfb705c0f109fb
# seed: 1605462553

# Time:  O(n^2 * r * logq), r = max(nums)
# Space: O(r)

# binary search, dp

class Solution2(object):
    def minZeroArray(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: int
        """
        dp = [{0} for _ in xrange(len(nums))]
        for i, (l, r, v) in enumerate(queries):
            if all(nums[i] in dp[i] for i in xrange(len(dp))):
                return i
            for j in xrange(l, r+1):
                dp[j] |= set(x+v for x in dp[j])
        return len(queries) if all(nums[i] in dp[i] for i in xrange(len(dp))) else -1