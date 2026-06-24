# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: most-expensive-item-that-can-not-be-bought
# source_path: LeetCode-Solutions-master/Python/most-expensive-item-that-can-not-be-bought.py
# solution_class: Solution2
# submission_id: ed4b11ce49d7e7cbf5e98fb27434c11e17606321
# seed: 4073121634

# Time:  O(1)
# Space: O(1)

# Chicken McNugget Theorem

class Solution2(object):
    def mostExpensiveItem(self, primeOne, primeTwo):
        """
        :type primeOne: int
        :type primeTwo: int
        :rtype: int
        """
        dp = [False]*max(primeOne, primeTwo)
        dp[0] = True
        result = 1
        for i in xrange(2, primeOne*primeTwo):
            dp[i%len(dp)] = dp[(i-primeOne)%len(dp)] or dp[(i-primeTwo)%len(dp)]
            if not dp[i%len(dp)]:
                result = i
        return result