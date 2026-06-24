# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: exclusive-time-of-functions
# source_path: LeetCode-Solutions-master/Python/exclusive-time-of-functions.py
# solution_class: Solution
# submission_id: 36b1121a0cdb5747a108ff1548dbe25095ec46c0
# seed: 30698762

# Time:  O(n)
# Space: O(n)

class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        result = [0] * n
        stk, prev = [], 0
        for log in logs:
            tokens = log.split(":")
            if tokens[1] == "start":
                if stk:
                    result[stk[-1]] += int(tokens[2]) - prev
                stk.append(int(tokens[0]))
                prev = int(tokens[2])
            else:
                result[stk.pop()] += int(tokens[2]) - prev + 1
                prev = int(tokens[2]) + 1
        return result