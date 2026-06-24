# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: lowest-common-ancestor-of-a-binary-search-tree
# source_path: LeetCode-Solutions-master/Python/lowest-common-ancestor-of-a-binary-search-tree.py
# solution_class: Solution
# submission_id: e9b1f8f3e3d5e57fd45d2b71b07a411d868547a1
# seed: 1058222037

# Time:  O(n)
# Space: O(1)

class Solution(object):
    # @param {TreeNode} root
    # @param {TreeNode} p
    # @param {TreeNode} q
    # @return {TreeNode}
    def lowestCommonAncestor(self, root, p, q):
        s, b = sorted([p.val, q.val])
        while not s <= root.val <= b:
            # Keep searching since root is outside of [s, b].
            root = root.left if s <= root.val else root.right
        # s <= root.val <= b.
        return root