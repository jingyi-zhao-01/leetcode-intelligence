# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: score-of-parentheses
# source_path: LeetCode-Solutions-master/Python/score-of-parentheses.py
# solution_class: Solution2
# submission_id: f24152f12036b561976809e5945a061a42ee9047
# seed: 4060939078

# Time:  O(n)
# Space: O(1)

class Solution2(object):
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        stack = [0]
        for c in S:
            if c == '(':
                stack.append(0)
            else:
                last = stack.pop()
                stack[-1] += max(1, 2*last)
        return stack[0]