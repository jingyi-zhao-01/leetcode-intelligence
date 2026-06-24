# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-substrings-with-only-1s
# source_path: LeetCode-Solutions-master/Python/number-of-substrings-with-only-1s.py
# solution_class: Solution
# submission_id: 88579ee6069a4226f4333782d8400941e1fc4f47
# seed: 4167508391

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def numSub(self, s):
        """
        :type s: str
        :rtype: int
        """
        MOD = 10**9+7
        result, count = 0, 0
        for c in s:
            count = count+1 if c == '1' else 0
            result = (result+count)%MOD
        return result