# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: lowest-common-ancestor-of-a-binary-tree-iv
# source_path: LeetCode-Solutions-master/Python/lowest-common-ancestor-of-a-binary-tree-iv.py
# solution_class: Solution2
# submission_id: b98185763d61f35376dc814b66bab7289d85450f
# seed: 3514803080

# Time:  O(n)
# Space: O(h)

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        pass

class Solution2(object):
    def lowestCommonAncestor(self, root, nodes):
        """
        :type root: TreeNode
        :type nodes: List[TreeNode]
        """
        def dfs(node, lookup):
            if not node or node in lookup:
                return node
            left, right = dfs(node.left, lookup), dfs(node.right, lookup)
            if left and right:
                return node
            return left or right
        
        return dfs(root, set(nodes))