# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: step-by-step-directions-from-a-binary-tree-node-to-another
# source_path: LeetCode-Solutions-master/Python/step-by-step-directions-from-a-binary-tree-node-to-another.py
# solution_class: Solution2
# submission_id: ec124adc5fb74a34240a93b45e30cc5a27563413
# seed: 2823096222

# Time:  O(n)
# Space: O(h)

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution2(object):
    def getDirections(self, root, startValue, destValue):
        """
        :type root: Optional[TreeNode]
        :type startValue: int
        :type destValue: int
        :rtype: str
        """
        def dfs(node, val, path):
            if node.val == val:
                return True
            if node.left and dfs(node.left, val, path):
                path.append('L')
            elif node.right and dfs(node.right, val, path):
                path.append('R')
            return path

        src, dst = [], []
        dfs(root, startValue, src)
        dfs(root, destValue, dst)
        while len(src) and len(dst) and src[-1] == dst[-1]:
            src.pop()
            dst.pop()
        dst.reverse()
        return "".join(['U']*len(src) + dst)