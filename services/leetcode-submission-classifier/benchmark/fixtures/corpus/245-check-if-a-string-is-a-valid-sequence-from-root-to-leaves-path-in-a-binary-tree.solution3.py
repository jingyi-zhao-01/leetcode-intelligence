# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: check-if-a-string-is-a-valid-sequence-from-root-to-leaves-path-in-a-binary-tree
# source_path: LeetCode-Solutions-master/Python/check-if-a-string-is-a-valid-sequence-from-root-to-leaves-path-in-a-binary-tree.py
# solution_class: Solution3
# submission_id: 5504fe0acb4319938519461bdec308c8482f7400
# seed: 529288829

# Time:  O(n)
# Space: O(w)

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# bfs solution

class Solution3(object):
    def isValidSequence(self, root, arr):
        """
        :type root: TreeNode
        :type arr: List[int]
        :rtype: bool
        """
        def dfs(node, arr, depth):
            if not node or depth == len(arr) or node.val != arr[depth]:
                return False
            if depth+1 == len(arr) and node.left == node.right:
                return True
            return dfs(node.left, arr, depth+1) or dfs(node.right, arr, depth+1)

        return dfs(root, arr, 0)