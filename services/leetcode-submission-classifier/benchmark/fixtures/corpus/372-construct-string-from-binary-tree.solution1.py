# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: construct-string-from-binary-tree
# source_path: LeetCode-Solutions-master/Python/construct-string-from-binary-tree.py
# solution_class: Solution
# submission_id: fb7d8b48b0bc6c439c7876265df4eeba5bfb35e6
# seed: 2715178696

# Time:  O(n)
# Space: O(h)

class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if not t: return ""
        s = str(t.val)
        if t.left or t.right:
            s += "(" + self.tree2str(t.left) + ")"
        if t.right:
            s += "(" + self.tree2str(t.right) + ")"
        return s