# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: time-needed-to-buy-tickets
# source_path: LeetCode-Solutions-master/Python/time-needed-to-buy-tickets.py
# solution_class: Solution
# submission_id: ccd4af80f728fdd4cc3914a9577d86a93135646e
# seed: 3330707879

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        """
        :type tickets: List[int]
        :type k: int
        :rtype: int
        """
        return sum(min(x, tickets[k] if i <= k else tickets[k]-1) for i, x in enumerate(tickets))