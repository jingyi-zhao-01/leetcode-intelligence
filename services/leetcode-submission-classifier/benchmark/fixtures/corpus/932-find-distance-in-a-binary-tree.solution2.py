# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-distance-in-a-binary-tree
# source_path: LeetCode-Solutions-master/Python/find-distance-in-a-binary-tree.py
# solution_class: Solution2
# submission_id: 5bbfc7a399d25c89364a60c686f57aa109e6a4da
# seed: 2574700845

# Time:  O(n)
# Space: O(h)

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        pass

class Solution2(object):
    def findDistance(self, root, p, q):
        """
        :type root: TreeNode
        :type p: int
        :type q: int
        :rtype: int
        """
        def dfs(node, p, q, result):
            if not node:
                return -1
            left = dfs(node.left, p, q, result)
            right = dfs(node.right, p, q, result)
            if node.val in (p, q):
                if left == right == -1:
                    return 0
                result[0] = left+1 if left != -1 else right+1
            if left != -1 and right != -1:
                result[0] = left+right+2
            elif left != -1:
                return left+1
            elif right != -1:
                return right+1
            return -1
        
        result = [0]
        dfs(root, p, q, result)
        return result[0]