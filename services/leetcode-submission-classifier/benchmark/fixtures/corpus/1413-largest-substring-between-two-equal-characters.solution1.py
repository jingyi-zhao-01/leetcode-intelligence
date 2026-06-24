# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: largest-substring-between-two-equal-characters
# source_path: LeetCode-Solutions-master/Python/largest-substring-between-two-equal-characters.py
# solution_class: Solution
# submission_id: f5973dae792c7c2fa73b52554181990548d6a737
# seed: 8941320

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def maxLengthBetweenEqualCharacters(self, s):
        """
        :type s: str
        :rtype: int
        """
        result, lookup = -1, {}
        for i, c in enumerate(s):
            result = max(result, i-lookup.setdefault(c, i)-1)
        return result