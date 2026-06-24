# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: insert-into-a-binary-search-tree
# source_path: LeetCode-Solutions-master/Python/insert-into-a-binary-search-tree.py
# solution_class: Solution2
# submission_id: 45d1b81479b73ba0aea62b90dd0c302bb7ad6500
# seed: 2583430553

# Time:  O(h)
# Space: O(1)

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution2(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root:
            root = TreeNode(val)
        else:
            if val <= root.val:
                root.left = self.insertIntoBST(root.left, val)
            else:
                root.right = self.insertIntoBST(root.right, val)
        return root