# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: generate-parentheses
# source_path: LeetCode-Solutions-master/Python/generate-parentheses.py
# solution_class: Solution
# submission_id: 9ff571eae3c9f0e55cc027d0b7b0546251b10222
# seed: 2532778622

# Time:  O(4^n / n^(3/2)) ~= Catalan numbers
# Space: O(n)

# iterative solution

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result, curr = [], []
        stk = [(1, (n, n))]
        while stk:
            step, args = stk.pop()
            if step == 1:
                left, right = args
                if left == 0 and right == 0:
                    result.append("".join(curr))
                if left < right:
                    stk.append((3, tuple()))
                    stk.append((1, (left, right-1)))
                    stk.append((2, (')')))
                if left > 0:
                    stk.append((3, tuple()))
                    stk.append((1, (left-1, right)))
                    stk.append((2, ('(')))
            elif step == 2:
                curr.append(args[0])
            elif step == 3:
                curr.pop()
        return result