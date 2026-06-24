# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: the-number-of-full-rounds-you-have-played
# source_path: LeetCode-Solutions-master/Python/the-number-of-full-rounds-you-have-played.py
# solution_class: Solution2
# submission_id: c9c0e1ea95a4ff91bdeaf51b61178682c3a32790
# seed: 4290632851

# Time:  O(1)
# Space: O(1)

class Solution2(object):
    def numberOfRounds(self, startTime, finishTime):
        """
        :type startTime: str
        :type finishTime: str
        :rtype: int
        """
        h1, m1 = map(int, startTime.split(":"))
        h2, m2 = map(int, finishTime.split(":"))
        if m1 > m2:
            h2 -= 1
            m2 += 60
        return max((h2-h1)%24*4 + m2//15 - (m1+15-1)//15, 0)