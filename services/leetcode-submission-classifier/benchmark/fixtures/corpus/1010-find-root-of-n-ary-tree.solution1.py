# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-root-of-n-ary-tree
# source_path: LeetCode-Solutions-master/Python/find-root-of-n-ary-tree.py
# solution_class: Solution
# submission_id: 27cd68c69aade697536cb90e951739593bd306d4
# seed: 3696240681

# Time:  O(n)
# Space: O(1)

# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        pass

class Solution(object):
    def findRoot(self, tree):
        """
        :type tree: List['Node']
        :rtype: 'Node'
        """
        root = 0
        for node in tree:
            root ^= id(node)
            for child in node.children:
                root ^= id(child)
        for node in tree:
            if id(node) == root:
                return node
        return None