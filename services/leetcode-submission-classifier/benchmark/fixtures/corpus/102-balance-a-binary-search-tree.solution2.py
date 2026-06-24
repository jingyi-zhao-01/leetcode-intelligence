# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: balance-a-binary-search-tree
# source_path: LeetCode-Solutions-master/Python/balance-a-binary-search-tree.py
# solution_class: Solution2
# submission_id: cf270288a7889da3a50eb30b9f25fb6dfcf1e08f
# seed: 811652717

# Time:  O(n)
# Space: O(h)

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# dfs solution with stack

class Solution2(object):
    def balanceBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def inorderTraversalHelper(node, arr):
            if not node:
                return
            inorderTraversalHelper(node.left, arr)
            arr.append(node.val)
            inorderTraversalHelper(node.right, arr)
        
        def sortedArrayToBstHelper(arr, i, j):
            if i >= j:
                return None
            mid = i + (j-i)//2
            node = TreeNode(arr[mid])
            node.left = sortedArrayToBstHelper(arr, i, mid)
            node.right = sortedArrayToBstHelper(arr, mid+1, j)
            return node
        
        arr = []
        inorderTraversalHelper(root, arr)
        return sortedArrayToBstHelper(arr, 0, len(arr))