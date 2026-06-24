# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-leaves-of-binary-tree
# source_path: LeetCode-Solutions-master/Python/find-leaves-of-binary-tree.py
# solution_class: Solution
# submission_id: b820031802c9c4940c71499d679a717dc33a929e
# seed: 1572954146

# Time:  O(n)
# Space: O(h)

class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        def findLeavesHelper(node, result):
            if not node:
                return -1
            level = 1 + max(findLeavesHelper(node.left, result), \
                            findLeavesHelper(node.right, result))
            if len(result) < level + 1:
                result.append([])
            result[level].append(node.val)
            return level

        result = []
        findLeavesHelper(root, result)
        return result