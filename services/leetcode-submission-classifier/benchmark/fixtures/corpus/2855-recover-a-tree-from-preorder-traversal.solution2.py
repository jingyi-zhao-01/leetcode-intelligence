# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: recover-a-tree-from-preorder-traversal
# source_path: LeetCode-Solutions-master/Python/recover-a-tree-from-preorder-traversal.py
# solution_class: Solution2
# submission_id: a973a33f3550e442507f23da3ca035378f33bdc8
# seed: 3246112225

# Time:  O(n)
# Space: O(h)

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# iterative stack solution

class Solution2(object):
    def recoverFromPreorder(self, S):
        """
        :type S: str
        :rtype: TreeNode
        """
        def recoverFromPreorderHelper(S, level, i):
            j = i[0]
            while j < len(S) and S[j] == '-':
                j += 1 
            if level != j - i[0]:
                return None
            i[0] = j
            while j < len(S) and S[j] != '-':
                j += 1
            node = TreeNode(int(S[i[0]:j]))
            i[0] = j
            node.left = recoverFromPreorderHelper(S, level+1, i)
            node.right = recoverFromPreorderHelper(S, level+1, i)
            return node

        return recoverFromPreorderHelper(S, 0, [0])