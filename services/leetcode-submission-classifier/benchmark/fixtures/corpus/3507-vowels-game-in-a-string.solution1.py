# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: vowels-game-in-a-string
# source_path: LeetCode-Solutions-master/Python/vowels-game-in-a-string.py
# solution_class: Solution
# submission_id: d2db5cf46ff785a05ce857122f7dbd2c8454f37e
# seed: 396703742

# Time:  O(n)
# Space: O(1)

# math

class Solution(object):
    def doesAliceWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return any(x in "aeiou" for x in s)