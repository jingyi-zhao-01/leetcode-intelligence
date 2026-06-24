# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-value-of-a-string-in-an-array
# source_path: LeetCode-Solutions-master/Python/maximum-value-of-a-string-in-an-array.py
# solution_class: Solution
# submission_id: d124de295df9cc355e9550f67f1ab02fa796b0f4
# seed: 1928755650

# Time:  O(n * l)
# Space: O(1)

# string

class Solution(object):
    def maximumValue(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        return max(int(s) if s.isdigit() else len(s) for s in strs)