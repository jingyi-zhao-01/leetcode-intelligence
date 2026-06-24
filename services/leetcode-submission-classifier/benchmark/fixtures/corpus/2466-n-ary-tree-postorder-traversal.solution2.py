# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: n-ary-tree-postorder-traversal
# source_path: LeetCode-Solutions-master/Python/n-ary-tree-postorder-traversal.py
# solution_class: Solution2
# submission_id: 67a26cf29df9426009acebb5e7401995beca38bb
# seed: 2368841941

# Time:  O(n)
# Space: O(h)

class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Solution2(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        def dfs(root, result):
            for child in root.children:
                if child:
                    dfs(child, result)
            result.append(root.val)
        
        result = []
        if root:
            dfs(root, result)
        return result