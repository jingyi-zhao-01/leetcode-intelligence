# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: binary-tree-preorder-traversal
# source_path: LeetCode-Solutions-master/Python/binary-tree-preorder-traversal.py
# solution_class: Solution
# submission_id: 90b590784fcc04d92067f5b2b9b758dc6d2a9010
# seed: 436659272

# Time:  O(n)
# Space: O(1)

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Morris Traversal Solution

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result, curr = [], root
        while curr:
            if curr.left is None:
                result.append(curr.val)
                curr = curr.right
            else:
                node = curr.left
                while node.right and node.right != curr:
                    node = node.right

                if node.right is None:
                    result.append(curr.val)
                    node.right = curr
                    curr = curr.left
                else:
                    node.right = None
                    curr = curr.right

        return result