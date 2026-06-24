# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: maximum-width-of-binary-tree
# source_path: LeetCode-Solutions-master/Python/maximum-width-of-binary-tree.py
# solution_class: Solution
# submission_id: 377a5995c7a56654f4d04e5aa2ec2f1c6ccd35e0
# seed: 4275880595

# Time:  O(n)
# Space: O(h)

class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node, i, depth, leftmosts):
            if not node:
                return 0
            if depth >= len(leftmosts):
                leftmosts.append(i)
            return max(i-leftmosts[depth]+1, \
                       dfs(node.left, i*2, depth+1, leftmosts), \
                       dfs(node.right, i*2+1, depth+1, leftmosts))

        leftmosts = []
        return dfs(root, 1, 0, leftmosts)