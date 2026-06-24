# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-lines-to-represent-a-line-chart
# source_path: LeetCode-Solutions-master/Python/minimum-lines-to-represent-a-line-chart.py
# solution_class: Solution
# submission_id: c70411421aa96eb9f4b53f9340c0663ceda80c0b
# seed: 2953659840

# Time:  O(nlogn)
# Space: O(1)

# sort, math, gcd

class Solution(object):
    def minimumLines(self, stockPrices):
        """
        :type stockPrices: List[List[int]]
        :rtype: int
        """
        def gcd(a, b):
            while b:
                a, b = b, a%b
            return a
    
        stockPrices.sort()
        result = 0
        prev = None
        for i in xrange(1, len(stockPrices)):
            dy, dx = stockPrices[i][1]-stockPrices[i-1][1], stockPrices[i][0]-stockPrices[i-1][0]
            g = gcd(dy, dx)
            if not prev or prev != (dy//g, dx//g):
                prev = (dy//g, dx//g)
                result += 1
        return result