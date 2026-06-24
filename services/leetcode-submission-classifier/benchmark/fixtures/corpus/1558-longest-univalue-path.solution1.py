# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: longest-univalue-path
# source_path: LeetCode-Solutions-master/Python/longest-univalue-path.py
# solution_class: Solution
# submission_id: 904970d37e426c1c73a80f2cbd910e3f5c8996bc
# seed: 2476856418

# Time:  O(n)
# Space: O(h)

class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        result = [0]
        def dfs(node):
            if not node:
                return 0
            left, right = dfs(node.left), dfs(node.right)
            left = (left+1) if node.left and node.left.val == node.val else 0
            right = (right+1) if node.right and node.right.val == node.val else 0
            result[0] = max(result[0], left+right)
            return max(left, right)

        dfs(root)
        return result[0]