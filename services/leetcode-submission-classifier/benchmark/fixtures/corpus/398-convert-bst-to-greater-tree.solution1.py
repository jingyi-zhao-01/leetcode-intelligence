# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: convert-bst-to-greater-tree
# source_path: LeetCode-Solutions-master/Python/convert-bst-to-greater-tree.py
# solution_class: Solution
# submission_id: b004bd22751a076fca6ae1ac87d1b0e88c9dab56
# seed: 1380523890

# Time:  O(n)
# Space: O(h)

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def convertBSTHelper(root, cur_sum):
            if not root:
                return cur_sum

            if root.right:
                cur_sum = convertBSTHelper(root.right, cur_sum)
            cur_sum += root.val
            root.val = cur_sum
            if root.left:
                cur_sum = convertBSTHelper(root.left, cur_sum)
            return cur_sum

        convertBSTHelper(root, 0)
        return root