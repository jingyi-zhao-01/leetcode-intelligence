# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: n-ary-tree-preorder-traversal
# source_path: LeetCode-Solutions-master/Python/n-ary-tree-preorder-traversal.py
# solution_class: Solution
# submission_id: 2ca294b6f8f0d8952200fc2778a0f13189f6ba56
# seed: 1460308204

# Time:  O(n)
# Space: O(h)

class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return []
        result, stack = [], [root]
        while stack:
            node = stack.pop()
            result.append(node.val)
            for child in reversed(node.children):
                if child:
                    stack.append(child)
        return result