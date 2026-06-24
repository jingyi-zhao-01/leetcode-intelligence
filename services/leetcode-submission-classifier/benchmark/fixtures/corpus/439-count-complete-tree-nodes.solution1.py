# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-complete-tree-nodes
# source_path: LeetCode-Solutions-master/Python/count-complete-tree-nodes.py
# solution_class: Solution
# submission_id: 6c977d3faef53099ef66c5bfe8b98aeb5f246bd9
# seed: 2699638345

# Time:  O(h * h) = O((logn)^2)
# Space: O(1)

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        pass

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def height(root):
            h = -1
            while root:
                h += 1
                root = root.left
            return h

        result, h = 0, height(root)
        while root:
            if height(root.right) == h-1:
                result += 2**h
                root = root.right
            else:
                result += 2**(h-1)
                root = root.left
            h -= 1
        return result