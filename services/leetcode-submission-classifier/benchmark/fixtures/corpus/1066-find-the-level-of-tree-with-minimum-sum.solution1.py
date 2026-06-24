# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-the-level-of-tree-with-minimum-sum
# source_path: LeetCode-Solutions-master/Python/find-the-level-of-tree-with-minimum-sum.py
# solution_class: Solution
# submission_id: cbb213460c243794ff22edc8d288d5f04843a3c5
# seed: 1647287078

# Time:  O(n)
# Space: O(w)

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        pass


# bfs

class Solution(object):
    def minimumLevel(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        q = [root]
        d = 1
        result = ((float("inf"), float("inf")))
        while q:
            new_q = []
            total = 0
            for u in q:
                if u.left:
                    new_q.append(u.left)
                if u.right:
                    new_q.append(u.right)
                total += u.val
            result = min(result, (total, d))
            q = new_q
            d += 1
        return result[-1]