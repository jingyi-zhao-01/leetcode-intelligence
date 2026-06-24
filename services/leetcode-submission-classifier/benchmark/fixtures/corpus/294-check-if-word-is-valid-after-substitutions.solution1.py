# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: check-if-word-is-valid-after-substitutions
# source_path: LeetCode-Solutions-master/Python/check-if-word-is-valid-after-substitutions.py
# solution_class: Solution
# submission_id: 3bfcbe19f3167eb265e2276a62f5d9adc6c55367
# seed: 2157222504

# Time:  O(n)
# Space: O(n)

class Solution(object):
    def isValid(self, S):
        """
        :type S: str
        :rtype: bool
        """
        stack = []
        for i in S:
            if i == 'c':
                if stack[-2:] == ['a', 'b']:
                    stack.pop()
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return not stack