# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: n-ary-tree-level-order-traversal
# source_path: LeetCode-Solutions-master/Python/n-ary-tree-level-order-traversal.py
# solution_class: Solution
# submission_id: f78bbaa79344a8f2d21c7cd10eefa4bed46299d3
# seed: 3992095095

# Time:  O(n)
# Space: O(w)

class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:
            return []
        result, q = [], [root]
        while q:
            result.append([node.val for node in q])
            q = [child for node in q for child in node.children if child]
        return result