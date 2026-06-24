# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-nearest-right-node-in-binary-tree
# source_path: LeetCode-Solutions-master/Python/find-nearest-right-node-in-binary-tree.py
# solution_class: Solution
# submission_id: 503673749a4f1f3ba9affa1f22960fb7f53e8880
# seed: 1407667491

# Time:  O(n)
# Space: O(w)

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        pass

class Solution(object):
    def findNeartestRightNode(self, root, u):
        """
        :type root: TreeNode
        :type u: TreeNode
        :rtype: TreeNode
        """
        q = [root]
        while q:
            new_q = []
            for i, node in enumerate(q):
                if node == u:
                    return q[i+1] if i+1 < len(q) else None
                if node.left:
                    new_q.append(node.left)
                if node.right:
                    new_q.append(node.right)
            q = new_q
        return None