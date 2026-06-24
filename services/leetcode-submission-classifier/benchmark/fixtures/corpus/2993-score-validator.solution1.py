# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: score-validator
# source_path: LeetCode-Solutions-master/Python/score-validator.py
# solution_class: Solution
# submission_id: 8bf865ea3bea78ad2598ac6cd5383dbf313e29d2
# seed: 433918340

# Time:  O(n)
# Space: O(1)

# freq table

class Solution(object):
    def scoreValidator(self, events):
        """
        :type events: List[str]
        :rtype: List[int]
        """
        result = [0]*2
        for x in events:
            if x == "W":
                result[1] += 1
                if result[1] == 10:
                    break
            elif x in ("WD", "NB"):
                result[0] += 1
            else:
                result[0] += int(x)
        return result