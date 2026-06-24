# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: license-key-formatting
# source_path: LeetCode-Solutions-master/Python/license-key-formatting.py
# solution_class: Solution
# submission_id: 355626bb0b9b2eabe34e6a66e85506dd4438b6dd
# seed: 1745896718

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        result = []
        for i in reversed(xrange(len(S))):
            if S[i] == '-':
                continue
            if len(result) % (K + 1) == K:
                result += '-'
            result += S[i].upper()
        return "".join(reversed(result))