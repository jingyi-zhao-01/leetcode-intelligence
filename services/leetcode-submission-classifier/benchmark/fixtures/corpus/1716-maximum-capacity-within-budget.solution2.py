# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-capacity-within-budget
# source_path: LeetCode-Solutions-master/Python/maximum-capacity-within-budget.py
# solution_class: Solution2
# submission_id: 91e31534fa148ae3267492c5422be30996d940f4
# seed: 493683747

# Time:  O(n + b)
# Space: O(b)

# hash table, prefix sum

class Solution2(object):
    def maxCapacity(self, costs, capacity, budget):
        """
        :type costs: List[int]
        :type capacity: List[int]
        :type budget: int
        :rtype: int
        """
        result = 0
        stk = []
        for i in sorted(xrange(len(costs)), key=lambda i: costs[i]):
            cost, cap = costs[i], capacity[i]
            if cost >= budget:
                break
            while stk and stk[-1][0]+cost >= budget:
                stk.pop()
            result = max(result, (stk[-1][1] if stk else 0)+cap)
            if not stk or stk[-1][1] < cap:
                stk.append((cost, cap))
        return result