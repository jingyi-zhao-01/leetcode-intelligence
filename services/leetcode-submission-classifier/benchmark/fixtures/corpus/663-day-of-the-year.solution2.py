# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: day-of-the-year
# source_path: LeetCode-Solutions-master/Python/day-of-the-year.py
# solution_class: Solution2
# submission_id: 53799e8b302e3cf11dfd4c9026cc2e5270fffd00
# seed: 845742069

# Time:  O(1)
# Space: O(1)

class Solution2(object):
    def dayOfYear(self, date):
        """
        :type date: str
        :rtype: int
        """
        def numberOfDays(Y, M):
            leap = 1 if ((Y % 4 == 0) and (Y % 100 != 0)) or (Y % 400 == 0) else 0
            return (28+leap if (M == 2) else 31-(M-1)%7%2)

        Y, M, result = map(int, date.split("-"))
        for i in xrange(1, M):
            result += numberOfDays(Y, i)
        return result