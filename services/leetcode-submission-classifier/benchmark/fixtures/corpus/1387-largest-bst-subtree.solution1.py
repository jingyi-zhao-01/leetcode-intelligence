# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: largest-bst-subtree
# source_path: LeetCode-Solutions-master/Python/largest-bst-subtree.py
# solution_class: Solution
# submission_id: f2d3a2ba9a03800cd053e182d0e22ec9377ec6f3
# seed: 3515810052

# Time:  O(n)
# Space: O(h)

class Solution(object):
    def largestBSTSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        max_size = [1]
        def largestBSTSubtreeHelper(root):
            if root.left is None and root.right is None:
                return 1, root.val, root.val

            left_size, left_min, left_max = 0, root.val, root.val
            if root.left is not None:
                left_size, left_min, left_max = largestBSTSubtreeHelper(root.left)

            right_size, right_min, right_max = 0, root.val, root.val
            if root.right is not None:
                right_size, right_min, right_max = largestBSTSubtreeHelper(root.right)

            size = 0
            if (root.left is None or left_size > 0) and \
               (root.right is None or right_size > 0) and \
               left_max <= root.val <= right_min:
                size = 1 + left_size + right_size
                max_size[0] = max(max_size[0], size)

            return size, left_min, right_max

        largestBSTSubtreeHelper(root)
        return max_size[0]