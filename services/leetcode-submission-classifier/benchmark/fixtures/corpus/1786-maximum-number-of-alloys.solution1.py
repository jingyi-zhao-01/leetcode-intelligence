# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-number-of-alloys
# source_path: LeetCode-Solutions-master/Python/maximum-number-of-alloys.py
# solution_class: Solution
# submission_id: 13a61ff367e728ccdbc7a26879dcff9e16f5aa34
# seed: 2509600455

# Time:  O(k * nlogn)
# Space: O(n)

# sort, math

class Solution(object):
    def maxNumberOfAlloys(self, n, k, budget, composition, stock, cost):
        """
        :type n: int
        :type k: int
        :type budget: int
        :type composition: List[List[int]]
        :type stock: List[int]
        :type cost: List[int]
        :rtype: int
        """
        def count(machine, budget):
            def cnt(x):
                return stock[x]//machine[x]
    
            idxs = range(n)
            idxs.sort(key=cnt)
            result = cnt(idxs[0])
            prefix = curr = discount = 0
            for i in xrange(n):
                curr += cost[idxs[i]]*machine[idxs[i]]
                discount += cost[idxs[i]]*(stock[idxs[i]]%machine[idxs[i]])
                if i+1 != n and cnt(idxs[i+1])-cnt(idxs[i]) == 0:
                    continue
                prefix += curr
                budget += discount
                curr = discount = 0
                mn = min((cnt(idxs[i+1])-cnt(idxs[i]) if i+1 < n else float("inf")), budget//prefix)
                if mn == 0:
                    break
                budget -= prefix*mn
                result += mn
            return result

        return max(count(machine, budget) for machine in composition)