# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: inorder-successor-in-bst
# source_path: LeetCode-Solutions-master/Python/inorder-successor-in-bst.py
# solution_class: Solution
# submission_id: 83c57964b23215a2bf363c8e63cfcb29f2711cb3
# seed: 1134573762

# Time:  O(h)
# Space: O(1)

class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        # If it has right subtree.
        if p and p.right:
            p = p.right
            while p.left:
                p = p.left
            return p

        # Search from root.
        successor = None
        while root and root != p:
            if root.val > p.val:
                successor = root
                root = root.left
            else:
                root = root.right

        return successor