# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: faulty-keyboard
# source_path: LeetCode-Solutions-master/Python/faulty-keyboard.py
# solution_class: Solution
# submission_id: 1daa8c673012985c7d31426755474bff8d3b5cae
# seed: 2441151125

# Time:  O(n)
# Space: O(n)

import collections


# deque

class Solution(object):
    def finalString(self, s):
        """
        :type s: str
        :rtype: str
        """
        dq = collections.deque()
        parity = 0
        for x in s:
            if x == 'i':
                parity ^= 1
            else:
                dq.appendleft(x) if parity else dq.append(x)
        if parity:
            dq.reverse()
        return "".join(dq)