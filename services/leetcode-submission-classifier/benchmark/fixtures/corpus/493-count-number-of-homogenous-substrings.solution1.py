# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-number-of-homogenous-substrings
# source_path: LeetCode-Solutions-master/Python/count-number-of-homogenous-substrings.py
# solution_class: Solution
# submission_id: e5f3620c086e927f42bd26a180ef72d6a28a592f
# seed: 923646344

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def countHomogenous(self, s):
        """
        :type s: str
        :rtype: int
        """
        MOD = 10**9+7
        result = cnt = 0
        for i in xrange(len(s)):
            if i and s[i-1] == s[i]:
                cnt += 1
            else:
                cnt = 1
            result = (result+cnt)%MOD
        return result