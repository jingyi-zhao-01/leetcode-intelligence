# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-number-of-people-that-can-be-caught-in-tag
# source_path: LeetCode-Solutions-master/Python/maximum-number-of-people-that-can-be-caught-in-tag.py
# solution_class: Solution
# submission_id: 38217750c0ca95584845748e0019e174cc72402f
# seed: 2500598023

# Time:  O(n)
# Space: O(1)

# greedy with two pointers solution

class Solution(object):
    def catchMaximumAmountofPeople(self, team, dist):
        """
        :type team: List[int]
        :type dist: int
        :rtype: int
        """
        result = i = j = 0
        while i < len(team) and j < len(team):
            if i+dist < j or team[i] != 1:
                i += 1
            elif j+dist < i or team[j] != 0:
                j += 1
            else:
                result += 1
                i += 1
                j += 1
        return result