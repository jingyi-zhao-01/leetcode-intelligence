# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: distribute-money-to-maximum-children
# source_path: LeetCode-Solutions-master/Python/distribute-money-to-maximum-children.py
# solution_class: Solution
# submission_id: 85b036dad77362941aad02a1638726cd0524da4d
# seed: 1632924396

# Time:  O(1)
# Space: O(1)

# greedy

class Solution(object):
    def distMoney(self, money, children):
        """
        :type money: int
        :type children: int
        :rtype: int
        """
        if money < children*1:
            return -1
        money -= children*1
        q, r = divmod(money, 7)
        return min(q, children) - int(q > children or (q == children and r != 0) or (q == children-1 and r == 3))