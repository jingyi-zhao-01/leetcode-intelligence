# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: paint-house-ii
# source_path: LeetCode-Solutions-master/Python/paint-house-ii.py
# solution_class: Solution2
# submission_id: 176100c030d240b232cfd36c9d926badf20257d0
# seed: 1119128271

# Time:  O(n * k)
# Space: O(k)

class Solution2(object):
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs:
            return 0

        n = len(costs)
        k = len(costs[0])
        min_cost = [costs[0], [0] * k]
        for i in xrange(1, n):
            smallest, second_smallest = float("inf"), float("inf")
            for j in xrange(k):
                if min_cost[(i - 1) % 2][j] < smallest:
                    smallest, second_smallest = min_cost[(i - 1) % 2][j], smallest
                elif min_cost[(i - 1) % 2][j] < second_smallest:
                    second_smallest = min_cost[(i - 1) % 2][j]
            for j in xrange(k):
                min_j = smallest if min_cost[(i - 1) % 2][j] != smallest else second_smallest
                min_cost[i % 2][j] = costs[i][j] + min_j

        return min(min_cost[(n - 1) % 2])