# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-good-nodes-in-binary-tree
# source_path: LeetCode-Solutions-master/Python/count-good-nodes-in-binary-tree.py
# solution_class: Solution
# submission_id: 92778255a85b28257737dbf63c8196f8e0ffd653
# seed: 1566289779

# Time:  O(n)
# Space: O(h)

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        result = 0
        stk = [(root, root.val)]
        while stk:
            node, curr_max = stk.pop()
            if not node:
                continue
            curr_max = max(curr_max, node.val)
            result += int(curr_max <= node.val)
            stk.append((node.right, curr_max))
            stk.append((node.left, curr_max))
        return result