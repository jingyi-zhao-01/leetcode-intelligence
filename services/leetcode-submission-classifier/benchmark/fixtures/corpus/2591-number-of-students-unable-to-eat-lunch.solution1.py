# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-students-unable-to-eat-lunch
# source_path: LeetCode-Solutions-master/Python/number-of-students-unable-to-eat-lunch.py
# solution_class: Solution
# submission_id: 9995ef43fdae766d26c67862b22937fd5d64518e
# seed: 188973613

# Time:  O(n)
# Space: O(1)

import collections

class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        count = collections.Counter(students)
        for i, s in enumerate(sandwiches):
            if not count[s]:
                break
            count[s] -= 1
        else:
            i = len(sandwiches)
        return len(sandwiches)-i