# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-largest-value-in-each-tree-row
# source_path: LeetCode-Solutions-master/Python/find-largest-value-in-each-tree-row.py
# solution_class: Solution
# submission_id: a3ff2f1e859b40cabd6035b05f5743bd5927eeb6
# seed: 3042200158

# Time:  O(n)
# Space: O(h)

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def largestValuesHelper(root, depth, result):
            if not root:
                return
            if depth == len(result):
                result.append(root.val)
            else:
                result[depth] = max(result[depth], root.val)
            largestValuesHelper(root.left, depth+1, result)
            largestValuesHelper(root.right, depth+1, result)

        result = []
        largestValuesHelper(root, 0, result)
        return result