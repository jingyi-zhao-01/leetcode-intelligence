# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: check-if-binary-string-has-at-most-one-segment-of-ones
# source_path: LeetCode-Solutions-master/Python/check-if-binary-string-has-at-most-one-segment-of-ones.py
# solution_class: Solution
# submission_id: b3b0560554cc150673a4323a30956eae917e3337
# seed: 533262325

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def checkOnesSegment(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return "01" not in s