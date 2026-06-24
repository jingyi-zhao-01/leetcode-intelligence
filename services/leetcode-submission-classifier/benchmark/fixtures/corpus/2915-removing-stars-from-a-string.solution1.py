# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: removing-stars-from-a-string
# source_path: LeetCode-Solutions-master/Python/removing-stars-from-a-string.py
# solution_class: Solution
# submission_id: 13798cd6768739aa47856ccefca66784d873dffe
# seed: 1930389561

# Time:  O(n)
# Space: O(n)

# stack

class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = []
        for c in s:
            if c == '*':
                result.pop()
            else:
                result.append(c)
        return "".join(result)