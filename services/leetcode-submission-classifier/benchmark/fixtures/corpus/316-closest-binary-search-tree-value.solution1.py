# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: closest-binary-search-tree-value
# source_path: LeetCode-Solutions-master/Python/closest-binary-search-tree-value.py
# solution_class: Solution
# submission_id: 0643eb460cf45c7d6397ec7de13cb2a8d57ee664
# seed: 4225091324

# Time:  O(h)
# Space: O(1)

class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        gap = float("inf")
        closest = float("inf")
        while root:
            if abs(root.val - target) < gap:
                gap = abs(root.val - target)
                closest = root.val
            if target == root.val:
                break
            elif target < root.val:
                root = root.left
            else:
                root = root.right
        return closest