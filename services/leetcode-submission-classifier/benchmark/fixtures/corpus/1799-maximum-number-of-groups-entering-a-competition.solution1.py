# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-number-of-groups-entering-a-competition
# source_path: LeetCode-Solutions-master/Python/maximum-number-of-groups-entering-a-competition.py
# solution_class: Solution
# submission_id: 044937ad9757b0eed16d78a7035b93427b1dac4c
# seed: 2842044392

# Time:  O(1)
# Space: O(1)

# math

class Solution(object):
    def maximumGroups(self, grades):
        """
        :type grades: List[int]
        :rtype: int
        """
        # (1+x)*x/2 <= len(grades)
        # => x <= ((1+8*len(grades))**0.5-1)/2.0
        return int(((1+8*len(grades))**0.5-1)/2.0)