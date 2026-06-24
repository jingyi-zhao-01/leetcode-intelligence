# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: print-binary-tree
# source_path: LeetCode-Solutions-master/Python/print-binary-tree.py
# solution_class: Solution
# submission_id: 172c10838a5143cd081f44e555a5a6a1fe6376ae
# seed: 293874227

# Time:  O(h * 2^h)
# Space: O(h * 2^h)

class Solution(object):
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        def getWidth(root):
            if not root:
                return 0
            return 2 * max(getWidth(root.left), getWidth(root.right)) + 1

        def getHeight(root):
            if not root:
                return 0
            return max(getHeight(root.left), getHeight(root.right)) + 1

        def preorderTraversal(root, level, left, right, result):
            if not root:
                return
            mid = left + (right-left)/2
            result[level][mid] = str(root.val)
            preorderTraversal(root.left, level+1, left, mid-1, result)
            preorderTraversal(root.right, level+1, mid+1, right, result)

        h, w = getHeight(root), getWidth(root)
        result = [[""] * w for _ in xrange(h)]
        preorderTraversal(root, 0, 0, w-1, result)
        return result