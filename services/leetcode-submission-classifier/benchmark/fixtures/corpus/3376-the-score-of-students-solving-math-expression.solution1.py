# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: the-score-of-students-solving-math-expression
# source_path: LeetCode-Solutions-master/Python/the-score-of-students-solving-math-expression.py
# solution_class: Solution
# submission_id: c37c830022774c27521bf99d19244622fb3a6a1a
# seed: 1891615503

# Time:  O(n^3 * a^2)
# Space: O(n^2)

class Solution(object):
    def scoreOfStudents(self, s, answers):
        """
        :type s: str
        :type answers: List[int]
        :rtype: int
        """
        MAX_ANS = 1000
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
        target = eval(s)
        return sum(5 if ans == target else 2 if ans in dp[0][-1] else 0 for ans in answers)