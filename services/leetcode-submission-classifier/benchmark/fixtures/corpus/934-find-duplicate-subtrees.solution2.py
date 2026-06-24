# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-duplicate-subtrees
# source_path: LeetCode-Solutions-master/Python/find-duplicate-subtrees.py
# solution_class: Solution2
# submission_id: 6f6958d950385e9f47fa40890c7236fbccbb9fa6
# seed: 1797776061

# Time:  O(n)
# Space: O(n)

import collections

class Solution2(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        def postOrderTraversal(node, lookup, result):
            if not node:
                return ""
            s = "(" + postOrderTraversal(node.left, lookup, result) + \
                str(node.val) + \
                postOrderTraversal(node.right, lookup, result) + \
                ")"
            if lookup[s] == 1:
                result.append(node)
            lookup[s] += 1
            return s

        lookup = collections.defaultdict(int)
        result = []
        postOrderTraversal(root, lookup, result)
        return result