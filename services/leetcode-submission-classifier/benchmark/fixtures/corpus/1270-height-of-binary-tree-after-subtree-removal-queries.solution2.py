# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: height-of-binary-tree-after-subtree-removal-queries
# source_path: LeetCode-Solutions-master/Python/height-of-binary-tree-after-subtree-removal-queries.py
# solution_class: Solution2
# submission_id: 654abeb4df3df629bac9d4f2809d743ee3ed075c
# seed: 1474217041

# Time:  O(n)
# Space: O(n)

import collections


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        pass


# iterative dfs

class Solution2(object):
    def treeQueries(self, root, queries):
        """
        :type root: Optional[TreeNode]
        :type queries: List[int]
        :rtype: List[int]
        """
        def dfs(curr, d):
            if not curr:
                return 0
            h = 1+max(dfs(curr.left, d+1), dfs(curr.right, d+1))
            if h > top[d][0]:
                top[d][0], top[d][1] = h, top[d][0]
            elif h > top[d][1]:
                top[d][1] = h
            depth[curr.val], height[curr.val] = d, h
            return h
        
        top = collections.defaultdict(lambda: [0]*2)
        depth, height = {}, {}
        dfs(root, 0)
        return [(depth[q]-1)+(top[depth[q]][0] if height[q] != top[depth[q]][0] else top[depth[q]][1]) for q in queries]