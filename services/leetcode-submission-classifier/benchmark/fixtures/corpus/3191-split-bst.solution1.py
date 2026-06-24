# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: split-bst
# source_path: LeetCode-Solutions-master/Python/split-bst.py
# solution_class: Solution
# submission_id: 2c61cafb0169dedae842fd4e3625a2a763e3cdca
# seed: 2401830308

# Time:  O(n)
# Space: O(h)

class Solution(object):
    def splitBST(self, root, V):
        """
        :type root: TreeNode
        :type V: int
        :rtype: List[TreeNode]
        """
        if not root:
            return None, None
        elif root.val <= V:
            result = self.splitBST(root.right, V)
            root.right = result[0]
            return root, result[1]
        else:
            result = self.splitBST(root.left, V)
            root.left = result[1]
            return result[0], root