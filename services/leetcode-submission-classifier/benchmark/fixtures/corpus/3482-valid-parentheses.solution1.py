# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: valid-parentheses
# source_path: LeetCode-Solutions-master/Python/valid-parentheses.py
# solution_class: Solution
# submission_id: 6d8d74c1a5a22b8b740742e3df49e45a75ee78b8
# seed: 2129777084

# Time:  O(n)
# Space: O(n)

class Solution(object):
    # @return a boolean
    def isValid(self, s):
        stack, lookup = [], {"(": ")", "{": "}", "[": "]"}
        for parenthese in s:
            if parenthese in lookup:
                stack.append(parenthese)
            elif len(stack) == 0 or lookup[stack.pop()] != parenthese:
                return False
        return len(stack) == 0