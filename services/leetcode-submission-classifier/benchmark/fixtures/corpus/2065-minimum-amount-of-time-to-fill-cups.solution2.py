# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-amount-of-time-to-fill-cups
# source_path: LeetCode-Solutions-master/Python/minimum-amount-of-time-to-fill-cups.py
# solution_class: Solution2
# submission_id: e224d4e6ce543cca0fa3e49d430c6c4ab69993ee
# seed: 3285355095

# Time:  O(1)
# Space: O(1)

# math

class Solution2(object):
    def fillCups(self, amount):
        """
        :type amount: List[int]
        :rtype: int
        """
        mx, total = max(amount), sum(amount)
        return mx if sum(amount)-mx <= mx else (total+1)//2