# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: average-waiting-time
# source_path: LeetCode-Solutions-master/Python/average-waiting-time.py
# solution_class: Solution
# submission_id: c34145998a580028554c1522e9b9d8acb1d1616a
# seed: 55768691

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def averageWaitingTime(self, customers):
        """
        :type customers: List[List[int]]
        :rtype: float
        """
        avai = wait = 0.0
        for a, t in customers:
            avai = max(avai, a)+t
            wait += avai-a
        return wait/len(customers)