# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: day-of-the-year
# source_path: LeetCode-Solutions-master/Python/day-of-the-year.py
# solution_class: Solution
# submission_id: e2e60e69cdaf670d5ba05de619ea7ee35539fc23
# seed: 270853820

# Time:  O(1)
# Space: O(1)

class Solution(object):
    def __init__(self):
        def dayOfMonth(M):
            return (28 if (M == 2) else 31-(M-1)%7%2)

        self.__lookup = [0]*12
        for M in xrange(1, len(self.__lookup)):
            self.__lookup[M] += self.__lookup[M-1]+dayOfMonth(M)
            
    def dayOfYear(self, date):
        """
        :type date: str
        :rtype: int
        """
        Y, M, D = map(int, date.split("-"))
        leap = 1 if M > 2 and (((Y % 4 == 0) and (Y % 100 != 0)) or (Y % 400 == 0)) else 0
        return self.__lookup[M-1]+D+leap