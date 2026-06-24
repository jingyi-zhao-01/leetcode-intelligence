# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-number-of-changes-to-make-binary-string-beautiful
# source_path: LeetCode-Solutions-master/Python/minimum-number-of-changes-to-make-binary-string-beautiful.py
# solution_class: Solution
# submission_id: 56676dac29a4868f53a4bae5809c080f7f56ef67
# seed: 3918402092

# Time:  O(n)
# Space: O(1)

# greedy

class Solution(object):
    def minChanges(self, s):
        """
        :type s: str
        :rtype: int
        """
        return sum(s[i] != s[i+1] for i in xrange(0, len(s), 2))