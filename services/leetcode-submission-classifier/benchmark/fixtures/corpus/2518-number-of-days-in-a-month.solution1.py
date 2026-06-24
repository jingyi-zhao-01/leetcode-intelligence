# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-days-in-a-month
# source_path: LeetCode-Solutions-master/Python/number-of-days-in-a-month.py
# solution_class: Solution
# submission_id: bb1ea96194d3dd1d73f22742f082b675e45fa8f7
# seed: 3612207830

# Time:  O(1)
# Space: O(1)

class Solution(object):
    def numberOfDays(self, Y, M):
        """
        :type Y: int
        :type M: int
        :rtype: int
        """
        leap = 1 if ((Y % 4 == 0) and (Y % 100 != 0)) or (Y % 400 == 0) else 0
        return (28+leap if (M == 2) else 31-(M-1)%7%2)