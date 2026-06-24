# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: diameter-of-binary-tree
# source_path: LeetCode-Solutions-master/Python/diameter-of-binary-tree.py
# solution_class: Solution2
# submission_id: ee5d7459698b761d97c10fb3d97a8a9bc7a56757
# seed: 354037435

# Time:  O(n)
# Space: O(h)

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution2(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root):
            if not root: 
                return 0, 0
            left_d, left_h = dfs(root.left)
            right_d, right_h = dfs(root.right)
            return max(left_d, right_d, left_h+right_h), 1+max(left_h, right_h)
 
        return dfs(root)[0]