# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: divide-a-string-into-groups-of-size-k
# source_path: LeetCode-Solutions-master/Python/divide-a-string-into-groups-of-size-k.py
# solution_class: Solution
# submission_id: ae3c6b98b8c86ac23f6a5bff93c381500a9df10a
# seed: 936979550

# Time:  O(n)
# Space: O(1)

# string

class Solution(object):
    def divideString(self, s, k, fill):
        """
        :type s: str
        :type k: int
        :type fill: str
        :rtype: List[str]
        """
        return [s[i:i+k] + fill*(i+k-len(s)) for i in xrange(0, len(s), k)]