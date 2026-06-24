# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: the-score-of-students-solving-math-expression
# source_path: LeetCode-Solutions-master/Python/the-score-of-students-solving-math-expression.py
# solution_class: Solution2
# submission_id: baa1637a038534def8340a62fb9249ee7aba8745
# seed: 3298025881

# Time:  O(n^3 * a^2)
# Space: O(n^2)

class Solution2(object):
    def scoreOfStudents(self, s, answers):
        """
        :type s: str
        :type answers: List[int]
        :rtype: int
        """
        MAX_ANS = 1000
        def evaluate(s):
            def compute(operands, operators):
                right, left = operands.pop(), operands.pop()
                operands.append(ops[operators.pop()](left, right))

            ops = {'+':operator.add, '*':operator.mul}
            precedence = {'+':0, '*':1}
            operands, operators, operand = [], [], 0
            for c in s:
                if c.isdigit():
                    operands.append(int(c))
                else:
                    while operators and precedence[operators[-1]] >= precedence[c]:
                        compute(operands, operators)
                    operators.append(c)
            while operators:
                compute(operands, operators)
            return operands[-1]

        n = (len(s)+1)//2
        dp = [[set() for _ in xrange(n)] for _ in xrange(n)]
        for i in xrange(n):
            dp[i][i].add(int(s[i*2]))
        for l in xrange(1, n):
            for left in xrange(n-l):
                right = left+l
                for k in xrange(left, right):
                    if s[2*k+1] == '+':
                        dp[left][right].update((x+y for x in dp[left][k] for y in dp[k+1][right] if x+y <= MAX_ANS))
                    else:
                        dp[left][right].update((x*y for x in dp[left][k] for y in dp[k+1][right] if x*y <= MAX_ANS))
        target = evaluate(s)
        return sum(5 if ans == target else 2 if ans in dp[0][-1] else 0 for ans in answers)