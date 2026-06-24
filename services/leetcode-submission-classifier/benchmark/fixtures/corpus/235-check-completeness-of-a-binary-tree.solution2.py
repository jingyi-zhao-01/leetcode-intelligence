# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: check-completeness-of-a-binary-tree
# source_path: LeetCode-Solutions-master/Python/check-completeness-of-a-binary-tree.py
# solution_class: Solution2
# submission_id: f28567958a8501cce9f28f13f827ccca17b95cd1
# seed: 2226495897

# Time:  O(n)
# Space: O(w)

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution2(object):
    def isCompleteTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        prev_level, current = [], [(root, 1)]
        count = 0
        while current:
            count += len(current)
            next_level = []
            for node, v in current:
                if not node:
                    continue
                next_level.append((node.left, 2*v))
                next_level.append((node.right, 2*v+1))
            prev_level, current = current, next_level
        return prev_level[-1][1] == count