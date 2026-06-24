# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: clone-n-ary-tree
# source_path: LeetCode-Solutions-master/Python/clone-n-ary-tree.py
# solution_class: Solution2
# submission_id: 5cce55fbb305922285d2de043ad1664263bca140
# seed: 3606000929

# Time:  O(n)
# Space: O(h)

# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

class Solution2(object):
    def cloneTree(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        def dfs(node):
            if not node:
                return None
            copy = Node(node.val)
            for child in node.children:
                copy.children.append(dfs(child))
            return copy
        
        return dfs(root)