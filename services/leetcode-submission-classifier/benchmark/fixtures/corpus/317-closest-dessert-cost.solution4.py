# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: closest-dessert-cost
# source_path: LeetCode-Solutions-master/Python/closest-dessert-cost.py
# solution_class: Solution4
# submission_id: 572629948ec9453954922ce0dc4551973e9e4b79
# seed: 751346914

# Time:  O(m * max(max_base, target + max_topping / 2)) ~= O(m * t)
# Space: O(max(max_base, target + max_topping / 2)) ~= O(t)

class Solution4(object):
    def closestCost(self, baseCosts, toppingCosts, target):
        """
        :type baseCosts: List[int]
        :type toppingCosts: List[int]
        :type target: int
        :rtype: int
        """
        max_count = 2
        combs = set([0])
        for t in toppingCosts:
            combs = set([c+i*t for c in combs for i in xrange(max_count+1)])
        result = float("inf")
        for b in baseCosts:
            for c in combs:
                result = min(result, b+c, key=lambda x: (abs(x-target), x))      
        return result