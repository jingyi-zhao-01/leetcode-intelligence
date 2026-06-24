# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: teemo-attacking
# source_path: LeetCode-Solutions-master/Python/teemo-attacking.py
# solution_class: Solution
# submission_id: b30117cabbab3049222f65a73758d912df328fec
# seed: 1745517989

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        result = duration * len(timeSeries)
        for i in xrange(1, len(timeSeries)):
            result -= max(0, duration - (timeSeries[i] - timeSeries[i-1]))
        return result