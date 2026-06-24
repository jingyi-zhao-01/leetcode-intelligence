# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: all-nodes-distance-k-in-binary-tree
# source_path: LeetCode-Solutions-master/Python/all-nodes-distance-k-in-binary-tree.py
# solution_class: Solution
# submission_id: 4bd17ac00c59515f741b7da965266ce3497c58c8
# seed: 380753626

# Time:  O(n)
# Space: O(n)

import collections

class Solution(object):
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        def dfs(parent, child, neighbors):
            if not child:
                return
            if parent:
                neighbors[parent.val].append(child.val)
                neighbors[child.val].append(parent.val)
            dfs(child, child.left, neighbors)
            dfs(child, child.right, neighbors)

        neighbors = collections.defaultdict(list)
        dfs(None, root, neighbors)
        bfs = [target.val]
        lookup = set(bfs)
        for _ in xrange(K):
            bfs = [nei for node in bfs
                   for nei in neighbors[node]
                   if nei not in lookup]
            lookup |= set(bfs)
        return bfs