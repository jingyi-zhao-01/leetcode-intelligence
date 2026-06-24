# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-ice-cream-bars
# source_path: LeetCode-Solutions-master/Python/maximum-ice-cream-bars.py
# solution_class: Solution
# submission_id: ddb8cc73beef746c26646c34fc954d04a5baff26
# seed: 1953754635

# Time:  O(nlogn)
# Space: O(1)

class Solution(object):
    def maxIceCream(self, costs, coins):
        """
        :type costs: List[int]
        :type coins: int
        :rtype: int
        """
        costs.sort()
        for i, c in enumerate(costs):
            coins -= c
            if coins < 0:
                return i
        return len(costs)