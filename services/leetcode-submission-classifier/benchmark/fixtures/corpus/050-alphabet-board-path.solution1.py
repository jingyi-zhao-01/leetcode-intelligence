# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: alphabet-board-path
# source_path: LeetCode-Solutions-master/Python/alphabet-board-path.py
# solution_class: Solution
# submission_id: 38150eaa19066b75ae94ba5237924ca795a59c5d
# seed: 3250577623

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def alphabetBoardPath(self, target):
        """
        :type target: str
        :rtype: str
        """
        x, y = 0, 0
        result = []
        for c in target:
            y1, x1 = divmod(ord(c)-ord('a'), 5)
            result.append('U' * max(y-y1, 0))
            result.append('L' * max(x-x1, 0))
            result.append('R' * max(x1-x, 0))
            result.append('D' * max(y1-y, 0))
            result.append('!')
            x, y = x1, y1
        return "".join(result)