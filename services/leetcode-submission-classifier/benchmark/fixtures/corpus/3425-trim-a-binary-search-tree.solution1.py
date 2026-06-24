# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: trim-a-binary-search-tree
# source_path: LeetCode-Solutions-master/Python/trim-a-binary-search-tree.py
# solution_class: Solution
# submission_id: d9e63417ce8f0e2f48a35e79605e26739b4e267e
# seed: 1301712694

# Time:  O(n)
# Space: O(h)

class Solution(object):
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        if not root:
            return None
        if root.val < L:
            return self.trimBST(root.right, L, R)
        if root.val > R:
            return self.trimBST(root.left, L, R)
        root.left, root.right = self.trimBST(root.left, L, R), self.trimBST(root.right, L, R)
        return root