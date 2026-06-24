# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: generate-parentheses
# source_path: LeetCode-Solutions-master/Python/generate-parentheses.py
# solution_class: Solution2
# submission_id: f1be0281aba3b2c5087454d6ef122e4e7d825457
# seed: 1728103608

# Time:  O(4^n / n^(3/2)) ~= Catalan numbers
# Space: O(n)

# iterative solution

class Solution2(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def generateParenthesisRecu(left, right, curr, result):
            if left == 0 and right == 0:
                result.append("".join(curr))
            if left > 0:
                curr.append('(')
                generateParenthesisRecu(left-1, right, curr, result)
                curr.pop()
            if left < right:
                curr.append(')')
                generateParenthesisRecu(left, right-1, curr, result)
                curr.pop()

        result = []
        generateParenthesisRecu(n, n, [], result)
        return result