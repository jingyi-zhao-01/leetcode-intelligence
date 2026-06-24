# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: flatten-binary-tree-to-linked-list
# source_path: LeetCode-Solutions-master/Python/flatten-binary-tree-to-linked-list.py
# solution_class: Solution
# submission_id: 8d9f494210bce9694bb68e34cf6c04f17db3fa9c
# seed: 2788683172

# Time:  O(n)
# Space: O(h), h is height of binary tree

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    # @param root, a tree node
    # @return nothing, do it in place
    def flatten(self, root):
        self.flattenRecu(root, None)

    def flattenRecu(self, root, list_head):
        if root:
            list_head = self.flattenRecu(root.right, list_head)
            list_head = self.flattenRecu(root.left, list_head)
            root.right = list_head
            root.left = None
            return root
        else:
            return list_head