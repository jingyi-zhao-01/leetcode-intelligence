# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: closest-nodes-queries-in-a-binary-search-tree
# source_path: LeetCode-Solutions-master/Python/closest-nodes-queries-in-a-binary-search-tree.py
# solution_class: Solution2
# submission_id: dac2d9fe028fdd9d68631942dfecc2973d604cf3
# seed: 3619864149

# Time:  O(n + qlogn)
# Space: O(n)

import bisect


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        pass


# iterative dfs, binary search

class Solution2(object):
    def closestNodes(self, root, queries):
        """
        :type root: Optional[TreeNode]
        :type queries: List[int]
        :rtype: List[List[int]]
        """
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            inorder.append(node.val)
            dfs(node.right)

        inorder = []
        dfs(root)
        result = []
        for q in queries:
            i = bisect.bisect_left(inorder, q)
            if i == len(inorder):
                result.append([inorder[i-1], -1])
            elif inorder[i] == q:
                result.append([inorder[i], inorder[i]])
            elif i-1 >= 0:
                result.append([inorder[i-1], inorder[i]])
            else:
                result.append([-1, inorder[i]])
        return result