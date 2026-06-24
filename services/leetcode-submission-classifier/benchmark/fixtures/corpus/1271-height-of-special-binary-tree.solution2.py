# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: height-of-special-binary-tree
# source_path: LeetCode-Solutions-master/Python/height-of-special-binary-tree.py
# solution_class: Solution2
# submission_id: 61340977407120c290bc6b5db6ce9af7bd1bf467
# seed: 4096911617

# Time:  O(n)
# Space: O(h)

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        pass


# dfs

class Solution2(object):
    def heightOfTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        result = -1
        q = [root]
        while q:
            new_q = []
            for u in q:
                if u.left and u.left.right != u:
                    new_q.append(u.left)
                if u.right and u.right.left != u:
                    new_q.append(u.right)
            q = new_q
            result += 1
        return result