# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-absolute-difference-queries
# source_path: LeetCode-Solutions-master/Python/minimum-absolute-difference-queries.py
# solution_class: Solution
# submission_id: 07c64fa13a2cc65d488818f1c17ef14f231bb7bd
# seed: 824735182

# Time:  O(r * (n + q)), r is the max of nums
# Space: O(r * n)

class Solution(object):
    def minDifference(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        INF = float("inf")
        prefix = [[0]*(max(nums)+1)]
        for num in nums:
            prefix.append(prefix[-1][:])
            prefix[-1][num] += 1
        result = []
        for l, r in queries:
            min_diff, prev = INF, -1
            for num in xrange(len(prefix[0])):
                if not (prefix[l][num] < prefix[r+1][num]):
                    continue
                if prev != -1:
                    min_diff = min(min_diff, num-prev)
                prev = num
            result.append(min_diff if min_diff != INF else -1)
        return result