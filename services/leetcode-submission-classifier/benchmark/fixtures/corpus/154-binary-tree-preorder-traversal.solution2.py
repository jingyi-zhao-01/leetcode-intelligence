# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: binary-tree-preorder-traversal
# source_path: LeetCode-Solutions-master/Python/binary-tree-preorder-traversal.py
# solution_class: Solution2
# submission_id: 13732b1a7f850377ceb4b248e3ce8202cafff7ac
# seed: 3920131733

# Time:  O(n)
# Space: O(1)

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Morris Traversal Solution

class Solution2(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result, stack = [], [(root, False)]
        while stack:
            root, is_visited = stack.pop()
            if root is None:
                continue
            if is_visited:
                result.append(root.val)
            else:
                stack.append((root.right, False))
                stack.append((root.left, False))
                stack.append((root, True))
        return result