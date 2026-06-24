# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-distance-between-bst-nodes
# source_path: LeetCode-Solutions-master/Python/minimum-distance-between-bst-nodes.py
# solution_class: Solution
# submission_id: 3e126fccdda58ac79c8a0b7b4a7f1378069ef742
# seed: 3001561814

# Time:  O(n)
# Space: O(h)

class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            self.result = min(self.result, node.val-self.prev)
            self.prev = node.val
            dfs(node.right)

        self.prev = float('-inf')
        self.result = float('inf')
        dfs(root)
        return self.result