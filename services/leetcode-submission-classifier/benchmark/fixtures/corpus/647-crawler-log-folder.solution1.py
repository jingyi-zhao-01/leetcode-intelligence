# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: crawler-log-folder
# source_path: LeetCode-Solutions-master/Python/crawler-log-folder.py
# solution_class: Solution
# submission_id: 19069c26910b4f8ff298fa8b41089b5a0f415a4f
# seed: 1673299990

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def minOperations(self, logs):
        """
        :type logs: List[str]
        :rtype: int
        """
        result = 0
        for log in logs:
            if log == "../":
                if result > 0:
                    result -= 1
            elif log != "./":
                result += 1
        return result