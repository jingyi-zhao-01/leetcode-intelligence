# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: lowest-common-ancestor-of-a-binary-tree
# source_path: LeetCode-Solutions-master/Python/lowest-common-ancestor-of-a-binary-tree.py
# solution_class: Solution
# submission_id: 7b93a374690b548fc13699e1ff7df401344388a0
# seed: 566714513

# Time:  O(n)
# Space: O(h)

class Solution(object):
    # @param {TreeNode} root
    # @param {TreeNode} p
    # @param {TreeNode} q
    # @return {TreeNode}
    def lowestCommonAncestor(self, root, p, q):
        if root in (None, p, q):
            return root

        left, right = [self.lowestCommonAncestor(child, p, q) \
                         for child in (root.left, root.right)]
        # 1. If the current subtree contains both p and q,
        #    return their LCA.
        # 2. If only one of them is in that subtree,
        #    return that one of them.
        # 3. If neither of them is in that subtree,
        #    return the node of that subtree.
        return root if left and right else left or right