# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: paint-house
# source_path: LeetCode-Solutions-master/Python/paint-house.py
# solution_class: Solution
# submission_id: 4b4efe40aafd8b11db210ac185698b9063293aa3
# seed: 2189190811

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs:
            return 0

        min_cost = [costs[0], [0, 0, 0]]

        n = len(costs)
        for i in xrange(1, n):
            min_cost[i % 2][0] = costs[i][0] + \
                                 min(min_cost[(i - 1) % 2][1], min_cost[(i - 1) % 2][2])
            min_cost[i % 2][1] = costs[i][1] + \
                                 min(min_cost[(i - 1) % 2][0], min_cost[(i - 1) % 2][2])
            min_cost[i % 2][2] = costs[i][2] + \
                                 min(min_cost[(i - 1) % 2][0], min_cost[(i - 1) % 2][1])

        return min(min_cost[(n - 1) % 2])