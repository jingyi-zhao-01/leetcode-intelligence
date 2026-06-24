# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-all-valid-pickup-and-delivery-options
# source_path: LeetCode-Solutions-master/Python/count-all-valid-pickup-and-delivery-options.py
# solution_class: Solution
# submission_id: b4d4ccade719812b181d4ec8c2d5c45b5bc9ac1e
# seed: 763230962

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def countOrders(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD = 10**9+7
        result = 1
        for i in reversed(xrange(2, 2*n+1, 2)):
            result = result * i*(i-1)//2 % MOD
        return result