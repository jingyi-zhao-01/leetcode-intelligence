# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: the-number-of-weak-characters-in-the-game
# source_path: LeetCode-Solutions-master/Python/the-number-of-weak-characters-in-the-game.py
# solution_class: Solution
# submission_id: 58d75c501f502fa643cd6562d639bd2f0fcc239e
# seed: 1730156395

# Time:  O(nlogn)
# Space: O(1)

class Solution(object):
    def numberOfWeakCharacters(self, properties):
        """
        :type properties: List[List[int]]
        :rtype: int
        """
        properties.sort(cmp=lambda a, b: cmp(b[1], a[1]) if a[0] == b[0] else cmp(a[0], b[0]))
        result = max_d = 0
        for a, d in reversed(properties):
            if d < max_d:
                result += 1
            max_d = max(max_d, d)
        return result