# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: correct-a-binary-tree
# source_path: LeetCode-Solutions-master/Python/correct-a-binary-tree.py
# solution_class: Solution
# submission_id: 0a7083929149596bd335d25877c0564955968336
# seed: 1280810540

# Time:  O(n)
# Space: O(w)

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        pass

class Solution(object):
    def correctBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        q = {root:None}
        while q:
            new_q = {}
            for node, parent in q.iteritems():
                if node.right in q:
                    if parent.left == node:
                        parent.left = None
                    else:
                        parent.right = None
                    return root
                if node.left:
                    new_q[node.left] = node
                if node.right:
                    new_q[node.right] = node
            q = new_q