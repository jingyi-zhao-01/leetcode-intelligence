# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-nesting-depth-of-the-parentheses
# source_path: LeetCode-Solutions-master/Python/maximum-nesting-depth-of-the-parentheses.py
# solution_class: Solution
# submission_id: 3cb2560016c8c78865e9a7a5021fec8ffc41458c
# seed: 4030911482

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = curr = 0
        for c in s:
            if c == '(':
                curr += 1
                result = max(result, curr)
            elif c == ')':
                curr -= 1
        return result