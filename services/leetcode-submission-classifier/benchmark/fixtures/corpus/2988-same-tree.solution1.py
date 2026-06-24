# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: same-tree
# source_path: LeetCode-Solutions-master/Python/same-tree.py
# solution_class: Solution
# submission_id: 5fc4da1977bf1e40eaa94466c678e4826a573a3f
# seed: 2134848002

# Time:  O(n)
# Space: O(h), h is height of binary tree

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    # @param p, a tree node
    # @param q, a tree node
    # @return a boolean
    def isSameTree(self, p, q):
        if p is None and q is None:
            return True

        if p is not None and q is not None:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        return False