# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: construct-binary-tree-from-preorder-and-inorder-traversal
# source_path: LeetCode-Solutions-master/Python/construct-binary-tree-from-preorder-and-inorder-traversal.py
# solution_class: Solution2
# submission_id: 8a2c586763868ed94589b106ee73c96b8737cabc
# seed: 2718947555

# Time:  O(n)
# Space: O(n)

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution2(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        preorder_iterator = iter(preorder)
        inorder_lookup = {n: i for i, n in enumerate(inorder)}
        
        def helper(start, end):
            if start > end:
                return None
            
            root_val = next(preorder_iterator)
            root = TreeNode(root_val)
            idx = inorder_lookup[root_val]
            root.left = helper(start, idx-1)
            root.right = helper(idx+1, end)
            return root

        return helper(0, len(inorder)-1)