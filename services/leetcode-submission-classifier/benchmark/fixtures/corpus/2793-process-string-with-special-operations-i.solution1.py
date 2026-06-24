# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: process-string-with-special-operations-i
# source_path: LeetCode-Solutions-master/Python/process-string-with-special-operations-i.py
# solution_class: Solution
# submission_id: 658eb7bf7f79e91d53b2ebc556f00d9979fb3c40
# seed: 2832583837

# Time:  O(r), r = len(result)
# Space: O(r)

import collections


# simulation, deque

class Solution(object):
    def processStr(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = collections.deque()
        right = True
        for x in s:
            if x == '*':
                if not result:
                    continue
                if right:
                    result.pop()
                else:
                    result.popleft()
            elif x == '#':
                result.extend(result)
            elif x == '%':
                right = not right
            else:
                if right:
                    result.append(x)
                else:
                    result.appendleft(x)
        if not right:
            result.reverse()
        return "".join(result)