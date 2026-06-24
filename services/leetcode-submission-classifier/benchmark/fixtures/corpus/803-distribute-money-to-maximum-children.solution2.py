# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: distribute-money-to-maximum-children
# source_path: LeetCode-Solutions-master/Python/distribute-money-to-maximum-children.py
# solution_class: Solution2
# submission_id: 40c9a5036bc80274e15226163518abec4a22bca7
# seed: 1074204656

# Time:  O(1)
# Space: O(1)

# greedy

class Solution2(object):
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
        if q > children:
            return children-1
        if q == children:
            return q-int(r != 0)
        if q == children-1:
            return q-int(r == 3)
        return q