# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: paint-house
# source_path: LeetCode-Solutions-master/Python/paint-house.py
# solution_class: Solution2
# submission_id: 6cc2c13f32a162f41a8eaf187965ab5d9c2bf698
# seed: 2442270935

# Time:  O(n)
# Space: O(1)

class Solution2(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs:
            return 0

        n = len(costs)
        for i in xrange(1, n):
            costs[i][0] += min(costs[i - 1][1], costs[i - 1][2])
            costs[i][1] += min(costs[i - 1][0], costs[i - 1][2])
            costs[i][2] += min(costs[i - 1][0], costs[i - 1][1])

        return min(costs[n - 1])