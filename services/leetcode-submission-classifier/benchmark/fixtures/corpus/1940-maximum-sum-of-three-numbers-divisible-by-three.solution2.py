# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-sum-of-three-numbers-divisible-by-three
# source_path: LeetCode-Solutions-master/Python/maximum-sum-of-three-numbers-divisible-by-three.py
# solution_class: Solution2
# submission_id: 3f8d3e732b5ed4fbd6d6bc546a67bd5d88c7a2e8
# seed: 1915492337

# Time:  O(n)
# Space: O(1)

# sort, math

class Solution2(object):
    def maximumSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        group = [[] for _ in xrange(3)]
        for x in nums:
            group[x%3].append(x)
        result = 0
        for g in group:
            g.sort(reverse=True)
            if len(g) >= 3:
                result = max(result, sum(g[i] for i in xrange(3)))
        if group[0] and group[1] and group[2]:
            result = max(result, group[0][0]+group[1][0]+group[2][0])
        return result