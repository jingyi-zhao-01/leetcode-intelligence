# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-cost-to-reach-every-position
# source_path: LeetCode-Solutions-master/Python/minimum-cost-to-reach-every-position.py
# solution_class: Solution
# submission_id: 2494658c09cd66db88bac9d234e19c828c09ea99
# seed: 1758518173

# Time:  O(n)
# Space: O(1)

# prefix sum

class Solution(object):
    def minCosts(self, cost):
        """
        :type cost: List[int]
        :rtype: List[int]
        """
        for i in xrange(1, len(cost)):
            cost[i] = min(cost[i], cost[i-1])
        return cost