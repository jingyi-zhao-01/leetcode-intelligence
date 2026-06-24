# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: total-distance-to-type-a-string-using-one-finger
# source_path: LeetCode-Solutions-master/Python/total-distance-to-type-a-string-using-one-finger.py
# solution_class: Solution
# submission_id: 7e74ab729286a3ec40c0aef73b90675a6a0ff33f
# seed: 238497818

# Time:  O(n + 26)
# Space: O(26)

# hash table
KEYBOARD = ("qwertyuiop", "asdfghjkl", "zxcvbnm")
LOOKUP = [None]*26
for r, row in enumerate(KEYBOARD):
    for c, x in enumerate(row):
        LOOKUP[ord(x)-ord('a')] = (r, c)

class Solution(object):
    def totalDistance(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        prev = LOOKUP[0]
        for x in s:
            curr = LOOKUP[ord(x)-ord('a')]
            result += abs(curr[0]-prev[0])+abs(curr[1]-prev[1])
            prev = curr
        return result