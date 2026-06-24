# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: reorder-log-files
# source_path: LeetCode-Solutions-master/Python/reorder-log-files.py
# solution_class: Solution
# submission_id: ed27d4fe1084303a11e5edeec02811a33a5a8efc
# seed: 3332183776

# Time:  O(nlogn * l), n is the length of files, l is the average length of strings
# Space: O(l)

class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        def f(log):
            i, content = log.split(" ", 1)
            return (0, content, i) if content[0].isalpha() else (1,)

        logs.sort(key=f)
        return logs