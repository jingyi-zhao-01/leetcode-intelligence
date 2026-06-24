# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-all-the-lonely-nodes
# source_path: LeetCode-Solutions-master/Python/find-all-the-lonely-nodes.py
# solution_class: Solution
# submission_id: 842ac87016f5a8962f7d66ae2c0158656c6b656c
# seed: 157490265

# Time:  O(n)
# Space: O(h)

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def getLonelyNodes(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        stk = [root]
        while stk:
            node = stk.pop()
            if not node:
                continue
            if node.left and not node.right:
                result.append(node.left.val)
            elif node.right and not node.left:
                result.append(node.right.val)
            stk.append(node.right)
            stk.append(node.left)
        return result