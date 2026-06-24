# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: binary-tree-upside-down
# source_path: LeetCode-Solutions-master/Python/binary-tree-upside-down.py
# solution_class: Solution2
# submission_id: eb8c976b0d8a6aded2b8d5a3066dd7c3f7207a79
# seed: 3383497096

# Time:  O(n)
# Space: O(1)

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution2(object):
    # @param root, a tree node
    # @return root of the upside down tree
    def upsideDownBinaryTree(self, root):
        return self.upsideDownBinaryTreeRecu(root, None)

    def upsideDownBinaryTreeRecu(self, p, parent):
        if p is None:
            return parent

        root = self.upsideDownBinaryTreeRecu(p.left, p)
        if parent:
            p.left = parent.right
        else:
            p.left = None
        p.right = parent

        return root