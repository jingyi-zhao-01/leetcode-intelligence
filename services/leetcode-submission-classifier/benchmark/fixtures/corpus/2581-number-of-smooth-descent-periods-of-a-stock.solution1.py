# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-smooth-descent-periods-of-a-stock
# source_path: LeetCode-Solutions-master/Python/number-of-smooth-descent-periods-of-a-stock.py
# solution_class: Solution
# submission_id: a0f1599c73178c6141275227e2c689e7acc293fa
# seed: 1963137118

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def getDescentPeriods(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        result = l = 0
        for i in xrange(len(prices)):
            l += 1
            if i+1 == len(prices) or prices[i]-1 != prices[i+1]:
                result += l*(l+1)//2
                l = 0
        return result