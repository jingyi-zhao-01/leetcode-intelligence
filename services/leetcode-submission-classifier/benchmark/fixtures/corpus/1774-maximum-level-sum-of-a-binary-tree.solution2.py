# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-level-sum-of-a-binary-tree
# source_path: LeetCode-Solutions-master/Python/maximum-level-sum-of-a-binary-tree.py
# solution_class: Solution2
# submission_id: 674e2058b740c27a82b09256f7dbd591a1ca9b5e
# seed: 215376879

# Time:  O(n)
# Space: O(h)

import collections


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# dfs solution

class Solution2(object):
    def maxLevelSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        result, level, max_total = 0, 1, float("-inf")
        q = collections.deque([root])
        while q:
            total = 0
            for _ in xrange(len(q)):
                node = q.popleft()
                total += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if total > max_total:
                result, max_total = level, total
            level += 1
        return result