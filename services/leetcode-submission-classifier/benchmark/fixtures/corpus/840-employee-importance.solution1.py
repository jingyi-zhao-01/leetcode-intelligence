# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: employee-importance
# source_path: LeetCode-Solutions-master/Python/employee-importance.py
# solution_class: Solution
# submission_id: 7650aa3570bfcdabc7ade86be3c7aa28a6fa1c56
# seed: 504866802

# Time:  O(n)
# Space: O(h)

import collections


"""
# Employee info
class Employee(object):
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""

class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        if employees[id-1] is None:
            return 0
        result = employees[id-1].importance
        for id in employees[id-1].subordinates:
            result += self.getImportance(employees, id)
        return result