# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: binary-tree-maximum-path-sum
# source_path: LeetCode-Solutions-master/Python/binary-tree-maximum-path-sum.py
# solution_class: Solution2
# submission_id: 949f167e4eb6aa4c91b256016f8df61b4a636835
# seed: 2902449985

# Time:  O(n)
# Space: O(h), h is height of binary tree

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution2(object):
    # @param root, a tree node
    # @return an integer
    def maxPathSum(self, root):
        def dfs(node):
            if not node:
                return (float("-inf"), 0)
            max_left, curr_left = dfs(node.left)
            max_right, curr_right = dfs(node.right)
            return (max(max_left, max_right, node.val+max(curr_left, 0)+max(curr_right, 0)),
                    node.val+max(curr_left, curr_right, 0))
        
        return dfs(root)[0]