# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: n-ary-tree-preorder-traversal
# source_path: LeetCode-Solutions-master/Python/n-ary-tree-preorder-traversal.py
# solution_class: Solution2
# submission_id: 8670f3c8711c1203fbcb4593a842928f4f3bfd68
# seed: 1187086421

# Time:  O(n)
# Space: O(h)

class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Solution2(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        def dfs(root, result):
            result.append(root.val)
            for child in root.children:
                if child:
                    dfs(child, result)
        
        result = []
        if root:
            dfs(root, result)
        return result