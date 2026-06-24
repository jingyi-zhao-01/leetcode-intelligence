# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: flip-binary-tree-to-match-preorder-traversal
# source_path: LeetCode-Solutions-master/Python/flip-binary-tree-to-match-preorder-traversal.py
# solution_class: Solution
# submission_id: 261c90825e2dae600a61ac398620d805b11603d0
# seed: 3088856007

# Time:  O(n)
# Space: O(h)

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

        

class Solution(object):
    def flipMatchVoyage(self, root, voyage):
        """
        :type root: TreeNode
        :type voyage: List[int]
        :rtype: List[int]
        """
        def dfs(root, voyage, i, result):
            if not root:
                return True
            if root.val != voyage[i[0]]:
                return False
            i[0] += 1
            if root.left and root.left.val != voyage[i[0]]:
                result.append(root.val)
                return dfs(root.right, voyage, i, result) and \
                       dfs(root.left, voyage, i, result)
            return dfs(root.left, voyage, i, result) and \
                   dfs(root.right, voyage, i, result)
        
        result = []
        return result if dfs(root, voyage, [0], result) else [-1]