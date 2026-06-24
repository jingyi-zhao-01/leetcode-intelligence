# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: construct-binary-tree-from-inorder-and-postorder-traversal
# source_path: LeetCode-Solutions-master/Python/construct-binary-tree-from-inorder-and-postorder-traversal.py
# solution_class: Solution
# submission_id: 11c403305923b6158259dfd28d6cbf4bdb01dcf1
# seed: 157609966

# Time:  O(n)
# Space: O(n)

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    # @param inorder, a list of integers
    # @param postorder, a list of integers
    # @return a tree node
    def buildTree(self, inorder, postorder):
        lookup = {}
        for i, num in enumerate(inorder):
            lookup[num] = i
        return self.buildTreeRecu(lookup, postorder, inorder, len(postorder), 0, len(inorder))

    def buildTreeRecu(self, lookup, postorder, inorder, post_end, in_start, in_end):
        if in_start == in_end:
            return None
        node = TreeNode(postorder[post_end - 1])
        i = lookup[postorder[post_end - 1]]
        node.left = self.buildTreeRecu(lookup, postorder, inorder, post_end - 1 - (in_end - i - 1), in_start, i)
        node.right = self.buildTreeRecu(lookup, postorder, inorder, post_end - 1, i + 1, in_end)
        return node