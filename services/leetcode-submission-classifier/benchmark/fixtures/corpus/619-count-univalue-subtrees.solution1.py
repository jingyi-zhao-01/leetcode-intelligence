# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-univalue-subtrees
# source_path: LeetCode-Solutions-master/Python/count-univalue-subtrees.py
# solution_class: Solution
# submission_id: b9b4ea51a849b8c65218928b265031ff65eb0f33
# seed: 1722126005

# Time:  O(n)
# Space: O(h)

class Solution(object):
    # @param {TreeNode} root
    # @return {integer}
    def countUnivalSubtrees(self, root):
        [is_uni, count] = self.isUnivalSubtrees(root, 0)
        return count

    def isUnivalSubtrees(self, root, count):
        if not root:
            return [True, count]

        [left, count] = self.isUnivalSubtrees(root.left, count)
        [right, count] = self.isUnivalSubtrees(root.right, count)
        if self.isSame(root, root.left, left) and \
           self.isSame(root, root.right, right):
                count += 1
                return [True, count]

        return [False, count]

    def isSame(self, root, child, is_uni):
        return not child or (is_uni and root.val == child.val)