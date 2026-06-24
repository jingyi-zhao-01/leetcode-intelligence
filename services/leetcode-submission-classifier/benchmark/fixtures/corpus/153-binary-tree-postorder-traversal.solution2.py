# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: binary-tree-postorder-traversal
# source_path: LeetCode-Solutions-master/Python/binary-tree-postorder-traversal.py
# solution_class: Solution2
# submission_id: 01eeae4079357106ae1a820ae2db5afb09801ac8
# seed: 1926895357

# Time:  O(n)
# Space: O(1)

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Morris Traversal Solution

class Solution2(object):
    def postorderTraversal(self, root):
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
                stack.append((root, True))
                stack.append((root.right, False))
                stack.append((root.left, False))
        return result