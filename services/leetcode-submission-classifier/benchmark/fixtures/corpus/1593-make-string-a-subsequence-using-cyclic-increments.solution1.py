# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: make-string-a-subsequence-using-cyclic-increments
# source_path: LeetCode-Solutions-master/Python/make-string-a-subsequence-using-cyclic-increments.py
# solution_class: Solution
# submission_id: 2ded1f1993e8f9505fb0cd89da73850de43b514e
# seed: 1650571997

# Time:  O(n)
# Space: O(1)

# greedy, two pointers

class Solution(object):
    def canMakeSubsequence(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: bool
        """
        i = 0
        for c in str1:
            if (ord(str2[i])-ord(c))%26 > 1:
                continue
            i += 1
            if i == len(str2):
                return True
        return False