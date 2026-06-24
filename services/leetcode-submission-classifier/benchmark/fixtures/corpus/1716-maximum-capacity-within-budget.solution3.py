# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-capacity-within-budget
# source_path: LeetCode-Solutions-master/Python/maximum-capacity-within-budget.py
# solution_class: Solution3
# submission_id: ae40f63ea509d8975d1df287bfa04220446f57f0
# seed: 587534590

# Time:  O(n + b)
# Space: O(b)

# hash table, prefix sum

class Solution3(object):
    def maxCapacity(self, costs, capacity, budget):
        """
        :type costs: List[int]
        :type capacity: List[int]
        :type budget: int
        :rtype: int
        """
        def binary_search_right(left, right, check):
            while left <= right:
                mid = left+(right-left)//2
                if not check(mid):
                    right = mid-1
                else:
                    left = mid+1
            return right

        idxs = sorted(xrange(len(costs)), key=lambda i: costs[i])
        prefix = [0]*(len(idxs)+1)
        for i, idx in enumerate(idxs):
            prefix[i+1] = max(prefix[i], capacity[idx])
        result = 0
        sorted_costs = [costs[i] for i in idxs]
        for i, idx in enumerate(idxs):
            cost, cap = costs[idx], capacity[idx]
            if cost >= budget:
                break
            j = bisect.bisect_left(sorted_costs, budget-cost, hi=i)-1
            result = max(result, prefix[j+1]+cap)
        return result