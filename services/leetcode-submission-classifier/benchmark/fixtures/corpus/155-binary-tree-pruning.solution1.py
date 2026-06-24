# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: binary-tree-pruning
# source_path: LeetCode-Solutions-master/Python/binary-tree-pruning.py
# solution_class: Solution
# submission_id: 18f700d14be562ec39acf9e659d6abfdeefceb99
# seed: 2306736064

# Time:  O(n)
# Space: O(h)

class Solution(object):
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        if not root.left and not root.right and root.val == 0:
            return None
        return root