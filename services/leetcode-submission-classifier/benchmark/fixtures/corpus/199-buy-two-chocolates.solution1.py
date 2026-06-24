# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: buy-two-chocolates
# source_path: LeetCode-Solutions-master/Python/buy-two-chocolates.py
# solution_class: Solution
# submission_id: 1df8bbaa433a908fdfd13f709a83ad04bc5f07b7
# seed: 3692562189

# Time:  O(n)
# Space: O(1)

# greedy

class Solution(object):
    def buyChoco(self, prices, money):
        """
        :type prices: List[int]
        :type money: int
        :rtype: int
        """
        i = min(xrange(len(prices)), key=lambda x: prices[x])
        j = min((j for j in xrange(len(prices)) if j != i), key=lambda x: prices[x])
        return money-(prices[i]+prices[j]) if prices[i]+prices[j] <= money else money