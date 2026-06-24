# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: perform-string-shifts
# source_path: LeetCode-Solutions-master/Python/perform-string-shifts.py
# solution_class: Solution
# submission_id: ed9b17e0c9db68b514be564dd047e903788617e9
# seed: 1787824987

# Time:  O(n + l)
# Space: O(l)

class Solution(object):
    def stringShift(self, s, shift):
        """
        :type s: str
        :type shift: List[List[int]]
        :rtype: str
        """
        left_shifts = 0
        for direction, amount in shift:
            if not direction:
                left_shifts += amount
            else:
                left_shifts -= amount
        left_shifts %= len(s)
        return s[left_shifts:] + s[:left_shifts]