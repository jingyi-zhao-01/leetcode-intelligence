# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: flip-string-to-monotone-increasing
# source_path: LeetCode-Solutions-master/Python/flip-string-to-monotone-increasing.py
# solution_class: Solution
# submission_id: 81ff05dbe034c251e70f37876cdba78a717b62ef
# seed: 3789435700

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def minFlipsMonoIncr(self, S):
        """
        :type S: str
        :rtype: int
        """
        flip0, flip1 = 0, 0
        for c in S:
            flip0 += int(c == '1')
            flip1 = min(flip0, flip1 + int(c == '0'))
        return flip1