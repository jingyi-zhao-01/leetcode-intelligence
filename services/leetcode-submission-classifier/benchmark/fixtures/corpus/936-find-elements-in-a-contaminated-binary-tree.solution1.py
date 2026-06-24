# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-elements-in-a-contaminated-binary-tree
# source_path: LeetCode-Solutions-master/Python/find-elements-in-a-contaminated-binary-tree.py
# solution_class: Solution
# submission_id: 2430a4ef5cf354bd20a48096b006e92329c0ec7c
# seed: 1450205116

# Time:  O(n)
# Space: O(h)

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class FindElements(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        def dfs(node, v, lookup):
            if not node:
                return
            node.val = v    
            lookup.add(v)
            dfs(node.left, 2*v+1, lookup)
            dfs(node.right, 2*v+2, lookup)

        self.__lookup = set()
        dfs(root, 0, self.__lookup)

    def find(self, target):
        """
        :type target: int
        :rtype: bool
        """
        return target in self.__lookup 
