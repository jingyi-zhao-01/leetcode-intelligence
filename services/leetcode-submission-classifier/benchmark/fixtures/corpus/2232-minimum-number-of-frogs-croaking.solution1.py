# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-number-of-frogs-croaking
# source_path: LeetCode-Solutions-master/Python/minimum-number-of-frogs-croaking.py
# solution_class: Solution
# submission_id: 135c1e182dd6011a288f3d202d4eb1fad3d75293
# seed: 2346749473

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def minNumberOfFrogs(self, croakOfFrogs):
        """
        :type croakOfFrogs: str
        :rtype: int
        """
        S = "croak"
        lookup = [0]*len(S)
        result = 0
        for c in croakOfFrogs:
            i = S.find(c)
            lookup[i] += 1
            if lookup[i-1]:
                lookup[i-1] -= 1
            elif i == 0:
                result += 1
            else:
                return -1
        return result if result == lookup[-1] else -1