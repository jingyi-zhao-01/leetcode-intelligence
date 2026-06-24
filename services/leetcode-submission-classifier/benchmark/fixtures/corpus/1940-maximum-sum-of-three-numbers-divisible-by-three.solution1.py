# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-sum-of-three-numbers-divisible-by-three
# source_path: LeetCode-Solutions-master/Python/maximum-sum-of-three-numbers-divisible-by-three.py
# solution_class: Solution
# submission_id: ea9e88d13587ce718d234c30bfa508b01564cf21
# seed: 1526181988

# Time:  O(n)
# Space: O(1)

# sort, math

class Solution(object):
    def maximumSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def add(arr, x):
            for i in xrange(len(arr)):
                if x > arr[i]:
                    arr[i], x = x, arr[i]
            if len(arr) != 3:
                arr.append(x)

        group = [[] for _ in xrange(3)]
        for x in nums:
            add(group[x%3], x)
        result = 0
        for g in group:
            if len(g) == 3:
                result = max(result, sum(g))
        if group[0] and group[1] and group[2]:
            result = max(result, group[0][0]+group[1][0]+group[2][0])
        return result