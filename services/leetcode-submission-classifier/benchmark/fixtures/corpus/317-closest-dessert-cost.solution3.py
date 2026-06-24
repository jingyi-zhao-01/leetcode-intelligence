# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: closest-dessert-cost
# source_path: LeetCode-Solutions-master/Python/closest-dessert-cost.py
# solution_class: Solution3
# submission_id: 97311223c6e16552a53f933358f482fbab3b04e1
# seed: 4189766888

# Time:  O(m * max(max_base, target + max_topping / 2)) ~= O(m * t)
# Space: O(max(max_base, target + max_topping / 2)) ~= O(t)

class Solution3(object):
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
        result, combs = float("inf"), sorted(combs)
        for b in baseCosts:
            idx = bisect.bisect_left(combs, target-b)
            if idx < len(combs):
                result = min(result, b+combs[idx], key=lambda x: (abs(x-target), x))
            if idx > 0:
                result = min(result, b+combs[idx-1], key=lambda x: (abs(x-target), x))        
        return result