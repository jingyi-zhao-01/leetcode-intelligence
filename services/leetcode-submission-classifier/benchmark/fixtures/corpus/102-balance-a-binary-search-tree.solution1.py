# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: balance-a-binary-search-tree
# source_path: LeetCode-Solutions-master/Python/balance-a-binary-search-tree.py
# solution_class: Solution
# submission_id: f528a7c43e77e2d312c87f0a3474e6edced2b015
# seed: 4040561892

# Time:  O(n)
# Space: O(h)

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# dfs solution with stack

class Solution(object):
    def balanceBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def inorderTraversal(root):
            result, stk = [], [(root, False)]
            while stk:
                node, is_visited = stk.pop()
                if node is None:
                    continue
                if is_visited:
                    result.append(node.val)
                else:
                    stk.append((node.right, False))
                    stk.append((node, True))
                    stk.append((node.left, False))
            return result
    
        def sortedArrayToBst(arr):
            ROOT, LEFT, RIGHT = range(3)
            result = [None]
            stk = [(0, len(arr), ROOT, result)]
            while stk:
                i, j, update, ret = stk.pop()
                if i >= j:
                    continue
                mid = i + (j-i)//2
                node = TreeNode(arr[mid])
                if update == ROOT:
                    ret[0] = node
                elif update == LEFT:
                    ret[0].left = node
                else:
                    ret[0].right = node
                stk.append((mid+1, j, RIGHT, [node]))
                stk.append((i, mid, LEFT, [node]))
            return result[0]
        
        return sortedArrayToBst(inorderTraversal(root))