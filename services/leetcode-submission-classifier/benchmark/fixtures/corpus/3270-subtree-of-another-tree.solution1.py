# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: subtree-of-another-tree
# source_path: LeetCode-Solutions-master/Python/subtree-of-another-tree.py
# solution_class: Solution
# submission_id: 6984721207b4912bb5c331546075cbb2e4fc7c1b
# seed: 3956115088

# Time:  O(m * n), m is the number of nodes of s, n is the number of nodes of t
# Space: O(h), h is the height of s

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        def isSame(x, y):
            if not x and not y:
                return True
            if not x or not y:
                return False
            return x.val == y.val and \
                   isSame(x.left, y.left) and \
                   isSame(x.right, y.right)

        def preOrderTraverse(s, t):
            return s != None and \
                   (isSame(s, t) or \
                    preOrderTraverse(s.left, t) or \
                    preOrderTraverse(s.right, t))

        return preOrderTraverse(s, t)