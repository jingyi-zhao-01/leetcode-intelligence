# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-deletions-to-make-string-balanced
# source_path: LeetCode-Solutions-master/Python/minimum-deletions-to-make-string-balanced.py
# solution_class: Solution
# submission_id: befa260a6caae7ed78e5a6a6b85b2640ab5094bd
# seed: 1936074117

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def minimumDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = b_cnt = 0
        for c in s:
            if c == 'b':
                b_cnt += 1
            elif b_cnt:
                b_cnt -= 1
                result += 1
        return result