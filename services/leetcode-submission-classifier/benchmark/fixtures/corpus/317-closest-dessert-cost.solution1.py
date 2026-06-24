# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: closest-dessert-cost
# source_path: LeetCode-Solutions-master/Python/closest-dessert-cost.py
# solution_class: Solution
# submission_id: d94810d93830ec9ebb11c291be8fd54fa8497e39
# seed: 125244590

# Time:  O(m * max(max_base, target + max_topping / 2)) ~= O(m * t)
# Space: O(max(max_base, target + max_topping / 2)) ~= O(t)

class Solution(object):
    def closestCost(self, baseCosts, toppingCosts, target):
        """
        :type baseCosts: List[int]
        :type toppingCosts: List[int]
        :type target: int
        :rtype: int
        """
        max_count = 2
        max_base, max_topping = max(baseCosts), max(toppingCosts)
        dp = [False]*(max(max_base, target+max_topping//2)+1)
        for b in baseCosts:
            dp[b] = True
        for t in toppingCosts:
            for _ in xrange(max_count):
                for i in reversed(xrange(len(dp)-t)):
                    if dp[i]:
                        dp[i+t] = True
        result = float("inf")
        for i in xrange(1, len(dp)):
            if not dp[i]:
                continue
            if abs(i-target) < abs(result-target):
                result = i
            if i >= target:
                break
        return result