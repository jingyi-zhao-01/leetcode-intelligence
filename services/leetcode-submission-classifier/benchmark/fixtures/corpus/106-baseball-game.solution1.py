# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: baseball-game
# source_path: LeetCode-Solutions-master/Python/baseball-game.py
# solution_class: Solution
# submission_id: bd59435a76a3c4cc636d9bf0c2ff49ef63d83e5d
# seed: 2738389507

# Time:  O(n)
# Space: O(n)

class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        history = []
        for op in ops:
            if op == '+':
                history.append(history[-1] + history[-2])
            elif op == 'D':
                history.append(history[-1] * 2)
            elif op == 'C':
                history.pop()
            else:
                history.append(int(op))
        return sum(history)