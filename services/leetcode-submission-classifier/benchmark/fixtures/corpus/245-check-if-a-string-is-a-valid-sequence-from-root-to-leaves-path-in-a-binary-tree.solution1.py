# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: check-if-a-string-is-a-valid-sequence-from-root-to-leaves-path-in-a-binary-tree
# source_path: LeetCode-Solutions-master/Python/check-if-a-string-is-a-valid-sequence-from-root-to-leaves-path-in-a-binary-tree.py
# solution_class: Solution
# submission_id: d66e394707380c387d632dec9ef0630b1ffd9787
# seed: 3658660652

# Time:  O(n)
# Space: O(w)

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# bfs solution

class Solution(object):
    def isValidSequence(self, root, arr):
        """
        :type root: TreeNode
        :type arr: List[int]
        :rtype: bool
        """
        q = [root]
        for depth in xrange(len(arr)):
            new_q = []
            while q:
                node = q.pop()
                if not node or node.val != arr[depth]:
                    continue
                if depth+1 == len(arr) and node.left == node.right:
                    return True
                new_q.extend(child for child in (node.left, node.right))
            q = new_q
        return False