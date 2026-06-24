# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: minimum-absolute-difference-in-bst
# source_path: LeetCode-Solutions-master/Python/minimum-absolute-difference-in-bst.py
# solution_class: Solution
# submission_id: 81d8a454c864608eb973439aa14496e3c80ea264
# seed: 326136082

# Time:  O(n)
# Space: O(h)

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def inorderTraversal(root, prev, result):
            if not root:
                return (result, prev)

            result, prev = inorderTraversal(root.left, prev, result)
            if prev: result = min(result, root.val - prev.val)
            return inorderTraversal(root.right, root, result)

        return inorderTraversal(root, None, float("inf"))[0]