# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: validate-binary-search-tree
# source_path: LeetCode-Solutions-master/Python/validate-binary-search-tree.py
# solution_class: Solution
# submission_id: 6e27fc2db879701f71a76ee4195a9f45476f1cdf
# seed: 1798277043

# Time:  O(n)
# Space: O(1)

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Morris Traversal Solution

class Solution(object):
    # @param root, a tree node
    # @return a list of integers
    def isValidBST(self, root):
        prev, cur = None, root
        while cur:
            if cur.left is None:
                if prev and prev.val >= cur.val:
                    return False
                prev = cur
                cur = cur.right
            else:
                node = cur.left
                while node.right and node.right != cur:
                    node = node.right

                if node.right is None:
                    node.right = cur
                    cur = cur.left
                else:
                    if prev and prev.val >= cur.val:
                        return False
                    node.right = None
                    prev = cur
                    cur = cur.right

        return True