# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-student-replacements
# source_path: LeetCode-Solutions-master/Python/number-of-student-replacements.py
# solution_class: Solution
# submission_id: 62845df0ea81be1ab51eb396b14059ca25ea8336
# seed: 3750004315

# Time:  O(n)
# Space: O(1)

# simulation

class Solution(object):
    def totalReplacements(self, ranks):
        """
        :type ranks: List[int]
        :rtype: int
        """
        result = -1
        mn = float("inf")
        for x in ranks:
            if x >= mn:
                continue
            mn = x
            result += 1
        return result