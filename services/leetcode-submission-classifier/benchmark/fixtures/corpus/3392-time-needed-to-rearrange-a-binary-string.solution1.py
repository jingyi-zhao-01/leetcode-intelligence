# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: time-needed-to-rearrange-a-binary-string
# source_path: LeetCode-Solutions-master/Python/time-needed-to-rearrange-a-binary-string.py
# solution_class: Solution
# submission_id: 420e4a1706eb63133a15b9ec8c73238fdabd4729
# seed: 3693861852

# Time:  O(n)
# Space: O(1)

# dp

class Solution(object):
    def secondsToRemoveOccurrences(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = cnt = 0
        for c in s: 
            if c == '0':
                cnt += 1
                continue
            if cnt:
                result = max(result+1, cnt)
        return result 