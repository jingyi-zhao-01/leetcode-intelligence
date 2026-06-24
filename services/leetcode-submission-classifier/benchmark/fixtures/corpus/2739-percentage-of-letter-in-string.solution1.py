# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: percentage-of-letter-in-string
# source_path: LeetCode-Solutions-master/Python/percentage-of-letter-in-string.py
# solution_class: Solution
# submission_id: 1d04488ef7099678ea64e46f10ef6a4211a18f74
# seed: 2060824611

# Time:  O(n)
# Space: O(1)

# string

class Solution(object):
    def percentageLetter(self, s, letter):
        """
        :type s: str
        :type letter: str
        :rtype: int
        """
        return 100*s.count(letter)//len(s)