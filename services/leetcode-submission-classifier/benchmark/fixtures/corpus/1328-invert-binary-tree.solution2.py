# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: invert-binary-tree
# source_path: LeetCode-Solutions-master/Python/invert-binary-tree.py
# solution_class: Solution2
# submission_id: 17d9160161022182c88dfc38e741f4cdd4c648f8
# seed: 3934374813

# Time:  O(n)
# Space: O(h)

import collections


# BFS solution.
class Queue(object):
    def __init__(self):
        self.data = collections.deque()

    def push(self, x):
        self.data.append(x)

    def peek(self):
        return self.data[0]

    def pop(self):
        return self.data.popleft()

    def size(self):
        return len(self.data)

    def empty(self):
        return len(self.data) == 0

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution2(object):
    # @param {TreeNode} root
    # @return {TreeNode}
    def invertTree(self, root):
        if root is not None:
            nodes = []
            nodes.append(root)
            while nodes:
                node = nodes.pop()
                node.left, node.right = node.right, node.left
                if node.left is not None:
                    nodes.append(node.left)
                if node.right is not None:
                    nodes.append(node.right)

        return root