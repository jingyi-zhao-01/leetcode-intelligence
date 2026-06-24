# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: closest-equal-element-queries
# source_path: LeetCode-Solutions-master/Python/closest-equal-element-queries.py
# solution_class: Solution
# submission_id: 5209375c19c19a1f5de4169c990a3495c2658eb1
# seed: 1200568225

# Time:  O(n)
# Space: O(n)

# hash table

class Solution(object):
    def solveQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[int]
        :rtype: List[int]
        """
        dist = [len(nums)]*len(nums)
        left = {}
        for i in xrange(2*len(nums)-1):
            x = nums[i%len(nums)]
            if x in left:
                dist[i%len(dist)] = min(dist[i%len(dist)], i-left[x])
            left[x] = i
        right = {}
        for i in reversed(xrange(2*len(nums)-1)):
            x = nums[i%len(nums)]
            if x in right:
                dist[i%len(dist)] = min(dist[i%len(dist)], right[x]-i)
            right[x] = i
        result = [-1]*len(queries)
        for i, x in enumerate(queries):
            if dist[x] < len(nums):
                result[i] = dist[x]
        return result