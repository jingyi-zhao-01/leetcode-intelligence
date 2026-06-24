# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: student-attendance-record-ii
# source_path: LeetCode-Solutions-master/Python/student-attendance-record-ii.py
# solution_class: Solution
# submission_id: 2913b1bf5452f9f99faad68dad10473c29d6e63c
# seed: 997279891

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def checkRecord(self, n):
        """
        :type n: int
        :rtype: int
        """
        M = 1000000007
        a0l0, a0l1, a0l2, a1l0, a1l1, a1l2 = 1, 0, 0, 0, 0, 0
        for i in xrange(n+1):
            a0l2, a0l1, a0l0 = a0l1, a0l0, (a0l0 + a0l1 + a0l2) % M
            a1l2, a1l1, a1l0 = a1l1, a1l0, (a0l0 + a1l0 + a1l1 + a1l2) % M
        return a1l0