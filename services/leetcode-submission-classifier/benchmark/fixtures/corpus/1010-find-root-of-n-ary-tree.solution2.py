# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-root-of-n-ary-tree
# source_path: LeetCode-Solutions-master/Python/find-root-of-n-ary-tree.py
# solution_class: Solution2
# submission_id: ea8c659b14ab7279971566ceb5da039a97e07889
# seed: 3612199672

# Time:  O(n)
# Space: O(1)

# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        pass

class Solution2(object):
    def findRoot(self, tree):
        """
        :type tree: List['Node']
        :rtype: 'Node'
        """
        root = 0
        for node in tree:
            root ^= node.val
            for child in node.children:
                root ^= child.val
        for node in tree:
            if node.val == root:
                return node
        return None