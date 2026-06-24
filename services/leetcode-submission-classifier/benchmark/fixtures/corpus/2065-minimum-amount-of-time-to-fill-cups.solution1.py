# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-amount-of-time-to-fill-cups
# source_path: LeetCode-Solutions-master/Python/minimum-amount-of-time-to-fill-cups.py
# solution_class: Solution
# submission_id: 6cd7c303cd12db9c6422e315bd5bb6070c170431
# seed: 3901734193

# Time:  O(1)
# Space: O(1)

# math

class Solution(object):
    def fillCups(self, amount):
        """
        :type amount: List[int]
        :rtype: int
        """
        return max(max(amount), (sum(amount)+1)//2)