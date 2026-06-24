# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: diameter-of-n-ary-tree
# source_path: LeetCode-Solutions-master/Python/diameter-of-n-ary-tree.py
# solution_class: Solution2
# submission_id: 5a31b8e297d9f6be06db3c6d0cb0500cd17993d3
# seed: 2672066708

# Time:  O(n)
# Space: O(h)

# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

class Solution2(object):
    def diameter(self, root):
        """
        :type root: 'Node'
        :rtype: int
        """
        def dfs(node):
            max_dia, max_depth = 0, 0
            for child in node.children:
                child_max_dia, child_max_depth = dfs(child)
                max_dia = max(max_dia, child_max_dia, max_depth+child_max_depth+1)
                max_depth = max(max_depth, child_max_depth+1)
            return max_dia, max_depth
        
        return dfs(root)[0]