# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-bottom-left-tree-value
# source_path: LeetCode-Solutions-master/Python/find-bottom-left-tree-value.py
# solution_class: Solution2
# submission_id: 573a4dfa91f97008c3669312b0a85829115c51cd
# seed: 189040619

# Time:  O(n)
# Space: O(h)

class Solution2(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        last_node, q = None, collections.deque([root])
        while q:
            last_node = q.popleft()
            q.extend([n for n in [last_node.right, last_node.left] if n])
        return last_node.val