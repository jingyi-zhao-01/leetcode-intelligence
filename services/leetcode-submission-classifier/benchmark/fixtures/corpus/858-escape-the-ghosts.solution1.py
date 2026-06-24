# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: escape-the-ghosts
# source_path: LeetCode-Solutions-master/Python/escape-the-ghosts.py
# solution_class: Solution
# submission_id: 1807c703f04e68d1b9c3708b9fc09dd271eab83f
# seed: 657367975

# Time:  O(n)
# Space: O(1)

class Solution(object):
    def escapeGhosts(self, ghosts, target):
        """
        :type ghosts: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        total = abs(target[0])+abs(target[1])
        return all(total < abs(target[0]-i)+abs(target[1]-j) for i, j in ghosts)