# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: restore-finishing-order
# source_path: LeetCode-Solutions-master/Python/restore-finishing-order.py
# solution_class: Solution
# submission_id: 9970d16579adbaf309c0bc0e570ad06ac9b38bf7
# seed: 3874035028

# Time:  O(n + min(8, n))
# Space: O(min(8, n))

# hash table

class Solution(object):
    def recoverOrder(self, order, friends):
        """
        :type order: List[int]
        :type friends: List[int]
        :rtype: List[int]
        """
        lookup = set(friends)
        return [x for x in order if x in lookup]