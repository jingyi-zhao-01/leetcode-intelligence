# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-the-highest-altitude
# source_path: LeetCode-Solutions-master/Python/find-the-highest-altitude.py
# solution_class: Solution
# submission_id: fe5c6267921425c1daf7e242df3888a79bea42a4
# seed: 1766350024

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        result = curr = 0
        for g in gain:
            curr += g
            result = max(result, curr)
        return result