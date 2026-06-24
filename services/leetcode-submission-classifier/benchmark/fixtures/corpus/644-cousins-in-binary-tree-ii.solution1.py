# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: cousins-in-binary-tree-ii
# source_path: LeetCode-Solutions-master/Python/cousins-in-binary-tree-ii.py
# solution_class: Solution
# submission_id: df82cff38b7ea114fd80213ab0184104593b659d
# seed: 507051858

# Time:  O(n)
# Space: O(w)

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        pass


# bfs

class Solution(object):
    def replaceValueInTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        q = [(root, root.val)]
        while q:
            new_q = []
            total = sum(node.val for node, _ in q)
            for node, x in q:
                node.val = total-x
                x = (node.left.val if node.left else 0) + (node.right.val if node.right else 0)
                if node.left:
                    new_q.append((node.left, x))
                if node.right:
                    new_q.append((node.right, x))
            q = new_q
        return root