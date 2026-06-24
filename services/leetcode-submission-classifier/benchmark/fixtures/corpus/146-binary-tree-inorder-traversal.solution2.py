# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: binary-tree-inorder-traversal
# source_path: LeetCode-Solutions-master/Python/binary-tree-inorder-traversal.py
# solution_class: Solution2
# submission_id: 3e76b8f845b08fd401ed4618a75deeb86ec0bf55
# seed: 2116308451

# Time:  O(n)
# Space: O(1)

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Morris Traversal Solution

class Solution2(object):
    def inorderTraversal(self, root):
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
                stack.append((root, True))
                stack.append((root.left, False))
        return result