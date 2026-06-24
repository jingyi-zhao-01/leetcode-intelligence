# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: the-number-of-full-rounds-you-have-played
# source_path: LeetCode-Solutions-master/Python/the-number-of-full-rounds-you-have-played.py
# solution_class: Solution
# submission_id: ccd58a1d7053f1b2fbac74ee80a4b5f17f6ddbb4
# seed: 180629135

# Time:  O(1)
# Space: O(1)

class Solution(object):
    def numberOfRounds(self, startTime, finishTime):
        """
        :type startTime: str
        :type finishTime: str
        :rtype: int
        """
        h1, m1 = map(int, startTime.split(":"))
        h2, m2 = map(int, finishTime.split(":"))
        start = h1*60+m1
        finish = h2*60+m2
        if start > finish:
            finish += 1440
        return max(finish//15-(start+15-1)//15, 0)