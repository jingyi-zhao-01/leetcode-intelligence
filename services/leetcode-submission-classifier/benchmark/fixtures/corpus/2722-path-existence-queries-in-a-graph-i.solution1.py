# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: path-existence-queries-in-a-graph-i
# source_path: LeetCode-Solutions-master/Python/path-existence-queries-in-a-graph-i.py
# solution_class: Solution
# submission_id: b796e56aa31835a8262437e6944bb869a357789b
# seed: 1625698043

# Time:  O(n + q)
# Space: O(n)

# prefix sum

class Solution(object):
    def pathExistenceQueries(self, n, nums, maxDiff, queries):
        """
        :type n: int
        :type nums: List[int]
        :type maxDiff: int
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        prefix = [0]*n
        for i in xrange(n-1):
            prefix[i+1] = prefix[i]+int(nums[i+1]-nums[i] > maxDiff)
        return [prefix[i] == prefix[j] for i, j in queries]