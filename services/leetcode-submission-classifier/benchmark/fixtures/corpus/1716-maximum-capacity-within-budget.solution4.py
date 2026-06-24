# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-capacity-within-budget
# source_path: LeetCode-Solutions-master/Python/maximum-capacity-within-budget.py
# solution_class: Solution4
# submission_id: 70fb1d3938176deb002cb24b452b2f6563501031
# seed: 1982601345

# Time:  O(n + b)
# Space: O(b)

# hash table, prefix sum

class Solution4(object):
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
        for i, idx in enumerate(idxs):
            cost, cap = costs[idx], capacity[idx]
            if cost >= budget:
                break
            j = binary_search_right(0, i-1, lambda x: costs[idxs[x]]+cost < budget)
            result = max(result, prefix[j+1]+cap)
        return result