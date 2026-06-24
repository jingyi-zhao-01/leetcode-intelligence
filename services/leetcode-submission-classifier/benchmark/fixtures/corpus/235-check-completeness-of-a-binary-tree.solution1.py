# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: check-completeness-of-a-binary-tree
# source_path: LeetCode-Solutions-master/Python/check-completeness-of-a-binary-tree.py
# solution_class: Solution
# submission_id: 02f32c08b521c590f390ea58a82cfdca750edfa9
# seed: 226606665

# Time:  O(n)
# Space: O(w)

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isCompleteTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        end = False
        current = [root]
        while current:
            next_level = []
            for node in current:
                if not node:
                    end = True
                    continue
                if end:
                    return False
                next_level.append(node.left)
                next_level.append(node.right)
            current = next_level
        return  True