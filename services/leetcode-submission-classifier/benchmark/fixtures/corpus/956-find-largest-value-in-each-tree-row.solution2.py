# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-largest-value-in-each-tree-row
# source_path: LeetCode-Solutions-master/Python/find-largest-value-in-each-tree-row.py
# solution_class: Solution2
# submission_id: ecf0886f9737e6a95e6553daa470d81ea4486455
# seed: 2877655938

# Time:  O(n)
# Space: O(h)

class Solution2(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        curr = [root]
        while any(curr):
            result.append(max(node.val for node in curr))
            curr = [child for node in curr for child in (node.left, node.right) if child]
        return result