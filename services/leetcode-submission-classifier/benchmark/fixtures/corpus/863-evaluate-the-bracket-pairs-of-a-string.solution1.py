# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: evaluate-the-bracket-pairs-of-a-string
# source_path: LeetCode-Solutions-master/Python/evaluate-the-bracket-pairs-of-a-string.py
# solution_class: Solution
# submission_id: f0db867d9ac8493af64b026ca933feecadc23e5c
# seed: 2737085153

# Time:  O(n + m)
# Space: O(n + m)

class Solution(object):
    def evaluate(self, s, knowledge):
        """
        :type s: str
        :type knowledge: List[List[str]]
        :rtype: str
        """
        lookup = {k: v for k, v in knowledge}
        result, curr = [], []
        has_pair = False
        for c in s:
            if c == '(':
                has_pair = True
            elif c == ')':
                has_pair = False
                result.append(lookup.get("".join(curr), '?'))
                curr = []
            elif has_pair:
                curr.append(c)
            else:
                result.append(c)
        return "".join(result)