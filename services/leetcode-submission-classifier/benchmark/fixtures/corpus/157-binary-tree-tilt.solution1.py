# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: binary-tree-tilt
# source_path: LeetCode-Solutions-master/Python/binary-tree-tilt.py
# solution_class: Solution
# submission_id: 8a27bfeba7e1e95c8a017b8050a7354c16a98a6c
# seed: 3783167858

# Time:  O(n)
# Space: O(n)

class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def postOrderTraverse(root, tilt):
            if not root:
                return 0, tilt
            left, tilt = postOrderTraverse(root.left, tilt)
            right, tilt = postOrderTraverse(root.right, tilt)
            tilt += abs(left-right)
            return left+right+root.val, tilt

        return postOrderTraverse(root, 0)[1]