# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: smallest-subtree-with-all-the-deepest-nodes
# source_path: LeetCode-Solutions-master/Python/smallest-subtree-with-all-the-deepest-nodes.py
# solution_class: Solution
# submission_id: 101edd195d6b50d30e78a02eab61577f02728ef5
# seed: 1574996842

# Time:  O(n)
# Space: O(h)

import collections

class Solution(object):
    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        Result = collections.namedtuple("Result", ("node", "depth"))

        def dfs(node):
            if not node:
                return Result(None, 0)
            left, right = dfs(node.left), dfs(node.right)
            if left.depth > right.depth:
                return Result(left.node, left.depth+1)
            if left.depth < right.depth:
                return Result(right.node, right.depth+1)
            return Result(node, left.depth+1)

        return dfs(root).node