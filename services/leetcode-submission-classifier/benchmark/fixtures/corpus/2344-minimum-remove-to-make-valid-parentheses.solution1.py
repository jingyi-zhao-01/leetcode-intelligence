# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-remove-to-make-valid-parentheses
# source_path: LeetCode-Solutions-master/Python/minimum-remove-to-make-valid-parentheses.py
# solution_class: Solution
# submission_id: db87a2adf29db966265f14fd6ec9b18b72913f49
# seed: 3807739150

# Time:  O(n)
# Space: O(n)

class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = list(s)
        count = 0
        for i, v in enumerate(result):
            if v == '(':
                count += 1
            elif v == ')':
                if count:
                    count -= 1
                else:
                    result[i] = ""
        if count:
            for i in reversed(xrange(len(result))):
                if result[i] == '(':
                    result[i] = ""
                    count -= 1
                    if not count:
                        break
        return "".join(result)