# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-moves-to-convert-string
# source_path: LeetCode-Solutions-master/Python/minimum-moves-to-convert-string.py
# solution_class: Solution
# submission_id: 9d73b1ca41cc0709bc4bc58aed7b90565f095126
# seed: 3457960816

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def minimumMoves(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = i = 0
        while i < len(s):
            if s[i] == 'X':
                result += 1
                i += 3
            else:
                i += 1
        return result