# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: check-if-string-is-decomposable-into-value-equal-substrings
# source_path: LeetCode-Solutions-master/Python/check-if-string-is-decomposable-into-value-equal-substrings.py
# solution_class: Solution
# submission_id: 0ff695765f20bee37f6f0f770f6a81c6417dd6d2
# seed: 2506011204

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def isDecomposable(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s)%3 != 2:
            return False
        for left in xrange(0, len(s), 3):
            if any(s[i] != s[i-1] for i in xrange(left+1, min(left+3, len(s)))):
                break            
        for right in reversed(xrange(left+1, len(s), 3)):
            if any(s[i] != s[i+1] for i in reversed(xrange(max(right-2, left), right))):
                break
        return right-left == 1