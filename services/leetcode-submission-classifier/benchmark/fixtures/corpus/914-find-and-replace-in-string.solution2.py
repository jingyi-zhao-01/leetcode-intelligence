# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-and-replace-in-string
# source_path: LeetCode-Solutions-master/Python/find-and-replace-in-string.py
# solution_class: Solution2
# submission_id: e19083c78f9b7ff90b63d608324a2c0c1f7ebaa5
# seed: 1907289653

# Time:  O(n + m), m is the number of targets
# Space: O(n)

class Solution2(object):
    def findReplaceString(self, S, indexes, sources, targets):
        """
        :type S: str
        :type indexes: List[int]
        :type sources: List[str]
        :type targets: List[str]
        :rtype: str
        """
        for i, s, t in sorted(zip(indexes, sources, targets), reverse=True):
            if S[i:i+len(s)] == s:
                S = S[:i] + t + S[i+len(s):]

        return S