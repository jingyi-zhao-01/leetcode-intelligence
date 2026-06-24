# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: find-duplicate-subtrees
# source_path: LeetCode-Solutions-master/Python/find-duplicate-subtrees.py
# solution_class: Solution
# submission_id: a53f08ad8c4d9abbdd0baa7eca7d40830988fa1b
# seed: 2307461107

# Time:  O(n)
# Space: O(n)

import collections

class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        def getid(root, lookup, trees):
            if not root:
                return -1
            node_id = lookup[root.val,
                             getid(root.left, lookup, trees),
                             getid(root.right, lookup, trees)]
            trees[node_id].append(root)
            return node_id

        trees = collections.defaultdict(list)
        lookup = collections.defaultdict()
        lookup.default_factory = lookup.__len__
        getid(root, lookup, trees)
        return [roots[0] for roots in trees.itervalues() if len(roots) > 1]