# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: zero-array-transformation-iv
# source_path: LeetCode-Solutions-master/Python/zero-array-transformation-iv.py
# solution_class: Solution
# submission_id: 583ce983fe448b2b104eb893a874fe8a83b241de
# seed: 853969199

# Time:  O(n^2 * r * logq), r = max(nums)
# Space: O(r)

# binary search, dp

class Solution(object):
    def minZeroArray(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: int
        """
        def binary_search(left, right, check):
            while left <= right:
                mid = left + (right-left)//2
                if check(mid):
                    right = mid-1
                else:
                    left = mid+1
            return left

        def check(l):
            def valid(arr, target):
                dp = [False]*(target+1)
                dp[0] = 1
                for i in xrange(len(arr)):
                    dp = [dp[j] or (j-arr[i] >= 0 and dp[j-arr[i]]) for j in xrange(target+1)]
                return dp[target]

            return all(valid([queries[j][2] for j in xrange(l) if queries[j][0] <= i <= queries[j][1]], nums[i]) for i in xrange(len(nums)))

        result = binary_search(0, len(queries), check)
        return result if result <= len(queries) else -1