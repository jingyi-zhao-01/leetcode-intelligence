# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: binary-tree-longest-consecutive-sequence-ii
# source_path: LeetCode-Solutions-master/Python/binary-tree-longest-consecutive-sequence-ii.py
# solution_class: Solution
# submission_id: 3263b591e32009ca3b7cbe07f6fe8b9f1bd32359
# seed: 59927679

# Time:  O(n)
# Space: O(h)

class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def longestConsecutiveHelper(root):
            if not root:
                return 0, 0
            left_len = longestConsecutiveHelper(root.left)
            right_len = longestConsecutiveHelper(root.right)
            cur_inc_len, cur_dec_len = 1, 1
            if root.left:
                if root.left.val == root.val + 1:
                    cur_inc_len = max(cur_inc_len, left_len[0] + 1)
                elif root.left.val == root.val - 1:
                    cur_dec_len = max(cur_dec_len, left_len[1] + 1)
            if root.right:
                if root.right.val == root.val + 1:
                    cur_inc_len = max(cur_inc_len, right_len[0] + 1)
                elif root.right.val == root.val - 1:
                    cur_dec_len = max(cur_dec_len, right_len[1] + 1)
            self.max_len = max(self.max_len, cur_dec_len + cur_inc_len - 1)
            return cur_inc_len, cur_dec_len

        self.max_len = 0
        longestConsecutiveHelper(root)
        return self.max_len