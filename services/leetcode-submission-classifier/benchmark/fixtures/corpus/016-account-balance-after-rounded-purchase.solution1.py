# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: account-balance-after-rounded-purchase
# source_path: LeetCode-Solutions-master/Python/account-balance-after-rounded-purchase.py
# solution_class: Solution
# submission_id: 386d3e5c2e1664a2b9c0de1a48090b6a002fc1a4
# seed: 3990666627

# Time:  O(1)
# Space: O(1)

# math

class Solution(object):
    def accountBalanceAfterPurchase(self, purchaseAmount):
        """
        :type purchaseAmount: int
        :rtype: int
        """
        return 100-(purchaseAmount+5)//10*10