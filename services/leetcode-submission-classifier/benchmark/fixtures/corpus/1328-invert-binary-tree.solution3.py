# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: invert-binary-tree
# source_path: LeetCode-Solutions-master/Python/invert-binary-tree.py
# solution_class: Solution3
# submission_id: 80df2ebbb38b9b69df6383f318aaff16cd9d7e21
# seed: 1269005567

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

class Solution3(object):
    # @param {TreeNode} root
    # @return {TreeNode}
    def invertTree(self, root):
        if root is not None:
            root.left, root.right = self.invertTree(root.right), \
                                    self.invertTree(root.left)

        return root