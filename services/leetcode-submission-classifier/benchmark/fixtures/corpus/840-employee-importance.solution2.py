# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: employee-importance
# source_path: LeetCode-Solutions-master/Python/employee-importance.py
# solution_class: Solution2
# submission_id: 33568055e557db3a98763941cbeb8d9d761ccb38
# seed: 1054312205

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

class Solution2(object):
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        result, q = 0, collections.deque([id])
        while q:
            curr = q.popleft()
            employee = employees[curr-1]
            result += employee.importance
            for id in employee.subordinates:
                q.append(id)
        return result