# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: check-if-a-string-is-a-valid-sequence-from-root-to-leaves-path-in-a-binary-tree
# source_path: LeetCode-Solutions-master/Python/check-if-a-string-is-a-valid-sequence-from-root-to-leaves-path-in-a-binary-tree.py
# solution_class: Solution2
# submission_id: f00f9d6818b5766eea236e363b17284b0f99813c
# seed: 2619782636

# Time:  O(n)
# Space: O(w)

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# bfs solution

class Solution2(object):
    def isValidSequence(self, root, arr):
        """
        :type root: TreeNode
        :type arr: List[int]
        :rtype: bool
        """
        s = [(root, 0)]
        while s:
            node, depth = s.pop()
            if not node or depth == len(arr) or node.val != arr[depth]:
                continue
            if depth+1 == len(arr) and node.left == node.right:
                return True
            s.append((node.right, depth+1))
            s.append((node.left, depth+1))
        return False