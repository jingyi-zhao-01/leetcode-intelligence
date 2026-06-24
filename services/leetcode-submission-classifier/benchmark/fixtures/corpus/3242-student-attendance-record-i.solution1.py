# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: student-attendance-record-i
# source_path: LeetCode-Solutions-master/Python/student-attendance-record-i.py
# solution_class: Solution
# submission_id: d48b31e40fe01eb93e8249bab254167b82074d48
# seed: 3344409809

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        count_A = 0
        for i in xrange(len(s)):
            if s[i] == 'A':
                count_A += 1
                if count_A == 2:
                    return False
            if i < len(s) - 2 and s[i] == s[i+1] == s[i+2] == 'L':
                return False
        return True