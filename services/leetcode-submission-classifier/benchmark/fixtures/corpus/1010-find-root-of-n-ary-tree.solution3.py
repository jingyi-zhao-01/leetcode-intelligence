# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-root-of-n-ary-tree
# source_path: LeetCode-Solutions-master/Python/find-root-of-n-ary-tree.py
# solution_class: Solution3
# submission_id: bf414e68101c920671cf2c7cdbcf587d81c468b6
# seed: 1026272992

# Time:  O(n)
# Space: O(1)

# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        pass

class Solution3(object):
    def findRoot(self, tree):
        """
        :type tree: List['Node']
        :rtype: 'Node'
        """
        root = 0
        for node in tree:
            root += node.val-sum(child.val for child in node.children)
        for node in tree:
            if node.val == root:
                return node
        return None