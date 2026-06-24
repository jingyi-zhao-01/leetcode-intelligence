# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximize-amount-after-two-days-of-conversions
# source_path: LeetCode-Solutions-master/Python/maximize-amount-after-two-days-of-conversions.py
# solution_class: Solution
# submission_id: 265390b02b3838f01d9c9130161ced126fb19f71
# seed: 1402707497

# Time:  O(n^2)
# Space: O(n)

# Bellman-Ford Algorithm

class Solution(object):
    def maxAmount(self, initialCurrency, pairs1, rates1, pairs2, rates2):
        """
        :type initialCurrency: str
        :type pairs1: List[List[str]]
        :type rates1: List[float]
        :type pairs2: List[List[str]]
        :type rates2: List[float]
        :rtype: float
        """
        def BellmanFord(dist, pairs, rates):
            for _ in xrange(len(pairs)):
                for i in xrange(len(pairs)):
                    dist[pairs[i][1]] = max(dist[pairs[i][1]], dist[pairs[i][0]]*rates[i])
                    dist[pairs[i][0]] = max(dist[pairs[i][0]], dist[pairs[i][1]]*(1/rates[i]))
        
        dist = collections.defaultdict(int)
        dist[initialCurrency] = 1.0
        BellmanFord(dist, pairs1, rates1)
        BellmanFord(dist, pairs2, rates2)
        return dist[initialCurrency]