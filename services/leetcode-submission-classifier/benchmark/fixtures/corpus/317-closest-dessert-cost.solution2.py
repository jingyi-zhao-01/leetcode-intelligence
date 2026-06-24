# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: closest-dessert-cost
# source_path: LeetCode-Solutions-master/Python/closest-dessert-cost.py
# solution_class: Solution2
# submission_id: 4aed21504b0d81c954c1b46d9f1ea2f93abd080b
# seed: 3717245399

# Time:  O(m * max(max_base, target + max_topping / 2)) ~= O(m * t)
# Space: O(max(max_base, target + max_topping / 2)) ~= O(t)

class Solution2(object):
    def closestCost(self, baseCosts, toppingCosts, target):
        """
        :type baseCosts: List[int]
        :type toppingCosts: List[int]
        :type target: int
        :rtype: int
        """
        max_count = 2
        def backtracking(toppingCosts, i, cost, target, lookup, result):
            if (i, cost) in lookup:
                return
            lookup.add((i, cost))
            if cost >= target or i == len(toppingCosts):
                if (abs(cost-target), cost) < (abs(result[0]-target), result[0]):
                    result[0] = cost
                return
            for j in xrange(max_count+1):
                backtracking(toppingCosts, i+1, cost+j*toppingCosts[i], target, lookup, result)

        result = [float("inf")]
        lookup = set()
        for b in baseCosts:
            backtracking(toppingCosts, 0, b, target, lookup, result)
        return result[0]