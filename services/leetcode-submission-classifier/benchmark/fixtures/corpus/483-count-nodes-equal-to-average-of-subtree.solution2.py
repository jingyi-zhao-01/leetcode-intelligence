# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-nodes-equal-to-average-of-subtree
# source_path: LeetCode-Solutions-master/Python/count-nodes-equal-to-average-of-subtree.py
# solution_class: Solution2
# submission_id: 82359dbd1167982d541acd3d5fb46dc0d9a81753
# seed: 2033320378

# Time:  O(n)
# Space: O(h)

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        pass


# dfs

class Solution2(object):
    def averageOfSubtree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def dfs(node):
            if not node:
                return [0]*3
            left = dfs(node.left)
            right = dfs(node.right)
            return [left[0]+right[0]+node.val,
                    left[1]+right[1]+1,
                    left[2]+right[2]+int((left[0]+right[0]+node.val)//(left[1]+right[1]+1) == node.val)]
        
        return dfs(root)[2]