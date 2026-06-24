# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-depth-of-n-ary-tree
# source_path: LeetCode-Solutions-master/Python/maximum-depth-of-n-ary-tree.py
# solution_class: Solution
# submission_id: 1977ba78bd43d0aca2234660a093c1fc6897dad0
# seed: 849653841

# Time:  O(n)
# Space: O(h)

class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if not root:
            return 0
        depth = 0
        for child in root.children:
            depth = max(depth, self.maxDepth(child))
        return 1+depth