# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-substrings-with-only-one-distinct-letter
# source_path: LeetCode-Solutions-master/Python/count-substrings-with-only-one-distinct-letter.py
# solution_class: Solution
# submission_id: 91afed6f3eff6cee224b1b5bfb8e18a499035653
# seed: 1074737980

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def countLetters(self, S):
        """
        :type S: str
        :rtype: int
        """
        result = len(S)
        left = 0
        for right in xrange(1, len(S)):
            if S[right] == S[left]:
                result += right-left
            else:
                left = right
        return result