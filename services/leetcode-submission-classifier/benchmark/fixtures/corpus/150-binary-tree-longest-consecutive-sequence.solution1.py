# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: binary-tree-longest-consecutive-sequence
# source_path: LeetCode-Solutions-master/Python/binary-tree-longest-consecutive-sequence.py
# solution_class: Solution
# submission_id: a88f0fb86f8db25d220c1719f4020f36ba8d9d7c
# seed: 1961642187

# Time:  O(n)
# Space: O(h)

class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max_len = 0

        def longestConsecutiveHelper(root):
            if not root:
                return 0

            left_len = longestConsecutiveHelper(root.left)
            right_len = longestConsecutiveHelper(root.right)

            cur_len = 1
            if root.left and root.left.val == root.val + 1:
                cur_len = max(cur_len, left_len + 1)
            if root.right and root.right.val == root.val + 1:
                cur_len = max(cur_len, right_len + 1)

            self.max_len = max(self.max_len, cur_len)

            return cur_len

        longestConsecutiveHelper(root)
        return self.max_len