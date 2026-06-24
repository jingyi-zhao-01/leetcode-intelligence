# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: flatten-binary-tree-to-linked-list
# source_path: LeetCode-Solutions-master/Python/flatten-binary-tree-to-linked-list.py
# solution_class: Solution2
# submission_id: 8a166cef78262ca67cb07bac3d44b22300d3de29
# seed: 2100425844

# Time:  O(n)
# Space: O(h), h is height of binary tree

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution2(object):
    list_head = None
    # @param root, a tree node
    # @return nothing, do it in place
    def flatten(self, root):
        if root:
            self.flatten(root.right)
            self.flatten(root.left)
            root.right = self.list_head
            root.left = None
            self.list_head = root