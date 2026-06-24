# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: climbing-stairs-ii
# source_path: LeetCode-Solutions-master/Python/climbing-stairs-ii.py
# solution_class: Solution
# submission_id: 1e882f1089f176b39b060b86fa005fa73fe7aa86
# seed: 1926953387

# Time:  O(n)
# Space: O(1)

# dp

class Solution(object):
    def climbStairs(self, n, costs):
        """
        :type n: int
        :type costs: List[int]
        :rtype: int
        """
        a, b, c = float("inf"), float("inf"), 0
        for i in xrange(n):
            a, b, c = b, c, costs[i]+min(a+3**2, b+2**2, c+1**2)
        return c