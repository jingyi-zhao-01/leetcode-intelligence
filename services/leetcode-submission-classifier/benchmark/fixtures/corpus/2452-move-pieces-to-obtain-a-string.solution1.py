# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: move-pieces-to-obtain-a-string
# source_path: LeetCode-Solutions-master/Python/move-pieces-to-obtain-a-string.py
# solution_class: Solution
# submission_id: 96c1d8f08fcdee4deae52963fa42dd7497d4584e
# seed: 3830265849

# Time:  O(n)
# Space: O(1)

# two pointers

class Solution(object):
    def canChange(self, start, target):
        """
        :type start: str
        :type target: str
        :rtype: bool
        """
        i = j = 0
        while True:
            while i < len(start) and start[i] == '_':
                i += 1
            while j < len(target) and target[j] == '_':
                j += 1
            if i == len(start) and j == len(target):
                break
            if i == len(start) or j == len(target) or start[i] != target[j] or \
               (start[i] == 'L' and i < j) or (start[i] == 'R' and i > j):
                    return False
            i += 1
            j += 1
        return True