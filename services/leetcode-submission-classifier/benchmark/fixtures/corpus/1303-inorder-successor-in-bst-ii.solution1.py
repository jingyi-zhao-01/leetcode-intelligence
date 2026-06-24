# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: inorder-successor-in-bst-ii
# source_path: LeetCode-Solutions-master/Python/inorder-successor-in-bst-ii.py
# solution_class: Solution
# submission_id: 2d0e3dc4e251db374bc2b77357812a567ffe818e
# seed: 604718114

# Time:  O(h)
# Space: O(1)

# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right, parent):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

        

class Solution(object):
    def inorderSuccessor(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return None
        
        if node.right:
            node = node.right
            while node.left:
                node = node.left
            return node
        
        while node.parent and node.parent.right is node:
            node = node.parent
        return node.parent