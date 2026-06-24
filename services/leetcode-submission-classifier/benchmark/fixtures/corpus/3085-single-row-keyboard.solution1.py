# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: single-row-keyboard
# source_path: LeetCode-Solutions-master/Python/single-row-keyboard.py
# solution_class: Solution
# submission_id: ddbf25b4c7256b4fe2b4130e8d03998612fb3bdc
# seed: 2724230265

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def calculateTime(self, keyboard, word):
        """
        :type keyboard: str
        :type word: str
        :rtype: int
        """
        lookup = {c:i for i, c in enumerate(keyboard)}
        result, prev = 0, 0
        for c in word:
            result += abs(lookup[c]-prev)
            prev = lookup[c]
        return result