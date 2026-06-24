# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-capacity-within-budget
# source_path: LeetCode-Solutions-master/Python/maximum-capacity-within-budget.py
# solution_class: Solution
# submission_id: 59e4ea406454c084625ceb79a26357cc6d049c75
# seed: 417929486

# Time:  O(n + b)
# Space: O(b)

# hash table, prefix sum

class Solution(object):
    def maxCapacity(self, costs, capacity, budget):
        """
        :type costs: List[int]
        :type capacity: List[int]
        :type budget: int
        :rtype: int
        """
        mid = (budget-1)//2
        lookup = [0]*budget
        for i in xrange(len(costs)):
            if costs[i] >= budget:
                continue
            lookup[costs[i]] = max(lookup[costs[i]], capacity[i])
        for i in xrange(mid):
            lookup[i+1] = max(lookup[i+1], lookup[i])
        result = mx = 0
        for i in xrange(len(costs)):
            if costs[i] > mid:
                continue
            result = max(result, mx+capacity[i])
            mx = max(mx, capacity[i])
        for i in xrange(mid+1, budget):
            result = max(result, lookup[i]+lookup[(budget-1)-i])
        return result