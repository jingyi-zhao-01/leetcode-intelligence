# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-number-of-chairs-in-a-waiting-room
# source_path: LeetCode-Solutions-master/Python/minimum-number-of-chairs-in-a-waiting-room.py
# solution_class: Solution
# submission_id: 3ba3b954515916bc3a6f3815887cec7cb3fd0756
# seed: 3019056830

# Time:  O(n)
# Space: O(1)

# simulation

class Solution(object):
    def minimumChairs(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = curr = 0
        for x in s:
            curr += +1 if x == "E" else -1
            result = max(result, curr)
        return result