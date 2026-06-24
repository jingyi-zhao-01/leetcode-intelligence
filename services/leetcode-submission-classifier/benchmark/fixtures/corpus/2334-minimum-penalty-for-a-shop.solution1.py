# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-penalty-for-a-shop
# source_path: LeetCode-Solutions-master/Python/minimum-penalty-for-a-shop.py
# solution_class: Solution
# submission_id: 6423e67af867b18c0d2539291df1b9c10fca84b5
# seed: 1055624565

# Time:  O(n)
# Space: O(1)

# greedy

class Solution(object):
    def bestClosingTime(self, customers):
        """
        :type customers: str
        :rtype: int
        """
        result = mx = curr = 0
        for i, x in enumerate(customers):
            curr += 1 if x == 'Y' else -1
            if curr > mx:
                mx = curr
                result = i+1
        return result