# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-hours-of-training-to-win-a-competition
# source_path: LeetCode-Solutions-master/Python/minimum-hours-of-training-to-win-a-competition.py
# solution_class: Solution
# submission_id: c0a94a6e8f094c80434eccb6d696fd97b72b12e5
# seed: 2005251691

# Time:  O(n)
# Space: O(1)

import itertools


# greedy

class Solution(object):
    def minNumberOfHours(self, initialEnergy, initialExperience, energy, experience):
        """
        :type initialEnergy: int
        :type initialExperience: int
        :type energy: List[int]
        :type experience: List[int]
        :rtype: int
        """
        result = 0
        for hp, ex in itertools.izip(energy, experience):
            inc1 = max((hp+1)-initialEnergy, 0)
            inc2 = max((ex+1)-initialExperience, 0)
            result += inc1+inc2
            initialEnergy += inc1-hp
            initialExperience += inc2+ex
        return result