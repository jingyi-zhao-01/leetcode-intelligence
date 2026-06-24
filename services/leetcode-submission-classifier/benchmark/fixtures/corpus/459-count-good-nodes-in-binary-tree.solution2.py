# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-good-nodes-in-binary-tree
# source_path: LeetCode-Solutions-master/Python/count-good-nodes-in-binary-tree.py
# solution_class: Solution2
# submission_id: d6faa9ca249f8666a613ed78dd8435d53c2ebf9c
# seed: 3417795430

# Time:  O(n)
# Space: O(h)

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution2(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node, curr_max):
            if not node:
                return 0
            curr_max = max(curr_max, node.val)
            return (int(curr_max <= node.val) +
                    dfs(node.left, curr_max) + dfs(node.right, curr_max))
        
        return dfs(root, root.val)