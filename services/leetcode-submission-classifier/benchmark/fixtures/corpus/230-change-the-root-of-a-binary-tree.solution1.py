# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: change-the-root-of-a-binary-tree
# source_path: LeetCode-Solutions-master/Python/change-the-root-of-a-binary-tree.py
# solution_class: Solution
# submission_id: ee9e48d0efd93d9f8d016672c7e63b785656c61f
# seed: 4111556809

# Time:  O(h)
# Space: O(1)

# Definition for a Node.
class Node:
    def __init__(self, val):
        pass

class Solution(object):
    def flipBinaryTree(self, root, leaf):
        """
        :type node: Node
        :rtype: Node
        """
        curr, parent = leaf, None
        while True:
            child = curr.parent
            curr.parent = parent
            if curr.left == parent:
                curr.left = None
            else:
                curr.right = None
            if curr == root:
                break
            if curr.left:
                curr.right = curr.left
            curr.left = child
            curr, parent = child, curr
        return leaf