# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: increasing-order-search-tree
# source_path: LeetCode-Solutions-master/Python/increasing-order-search-tree.py
# solution_class: Solution
# submission_id: 8a459e2ed9dd85763351da6c1d7d8cbac3820be8
# seed: 1985958695

# Time:  O(n)
# Space: O(h)

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def increasingBSTHelper(root, tail):
            if not root:
                return tail
            result = increasingBSTHelper(root.left, root)
            root.left = None
            root.right = increasingBSTHelper(root.right, tail)
            return result
        return increasingBSTHelper(root, None)