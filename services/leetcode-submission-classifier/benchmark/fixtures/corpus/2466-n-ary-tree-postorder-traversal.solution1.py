# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: n-ary-tree-postorder-traversal
# source_path: LeetCode-Solutions-master/Python/n-ary-tree-postorder-traversal.py
# solution_class: Solution
# submission_id: f2fcea78c53038287f579da76435ba5a9e2041d4
# seed: 48246102

# Time:  O(n)
# Space: O(h)

class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Solution(object):
    def postorder(self, root):
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
            for child in node.children:
                if child:
                    stack.append(child)
        return result[::-1]