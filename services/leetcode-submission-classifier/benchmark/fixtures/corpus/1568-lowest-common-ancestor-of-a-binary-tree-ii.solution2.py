# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: lowest-common-ancestor-of-a-binary-tree-ii
# source_path: LeetCode-Solutions-master/Python/lowest-common-ancestor-of-a-binary-tree-ii.py
# solution_class: Solution2
# submission_id: f8b029a1c0a31a4a3baaf8e913b17c78685469dc
# seed: 321979079

# Time:  O(n)
# Space: O(h)

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        pass

class Solution2(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """        
        def dfs(node, p, q, result):
            if not node:
                return 0
            left = dfs(node.left, p, q, result)
            right = dfs(node.right, p, q, result)
            curr = int(node == p or node == q)
            if curr+left+right == 2 and not result[0]:
                result[0] = node
            return curr+left+right

        result = [0]
        dfs(root, p, q, result)
        return result[0]