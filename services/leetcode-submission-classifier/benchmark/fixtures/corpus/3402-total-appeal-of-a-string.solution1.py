# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: total-appeal-of-a-string
# source_path: LeetCode-Solutions-master/Python/total-appeal-of-a-string.py
# solution_class: Solution
# submission_id: 9554c639d2423dbc27e53c8426ca657f902db7c9
# seed: 875914356

# Time:  O(n)
# Space: O(26)

# combinatorics

class Solution(object):
    def appealSum(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = curr = 0
        lookup = [-1]*26
        for i, c in enumerate(s):
            result += (i-lookup[ord(c)-ord('a')])*(len(s)-i)
            lookup[ord(c)-ord('a')] = i
        return result