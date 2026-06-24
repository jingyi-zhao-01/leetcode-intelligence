# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-flips-to-make-binary-string-coherent
# source_path: LeetCode-Solutions-master/Python/minimum-flips-to-make-binary-string-coherent.py
# solution_class: Solution
# submission_id: 1e9afc3a338b9af4ffda878c477cfdec754835e5
# seed: 3031468049

# Time:  O(n)
# Space: O(1)

# greedy, case works

class Solution(object):
    def minFlips(self, s):
        """
        :type s: str
        :rtype: int
        """
        cnt0 = s.count('0')
        cnt1 = len(s)-cnt0
        return min(cnt0, max(cnt1-1, 0), max(cnt1-(s[0] == '1')-(s[-1] == '1'), 0))