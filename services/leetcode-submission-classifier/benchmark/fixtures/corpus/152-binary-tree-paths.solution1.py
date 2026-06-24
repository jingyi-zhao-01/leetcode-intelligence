# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: binary-tree-paths
# source_path: LeetCode-Solutions-master/Python/binary-tree-paths.py
# solution_class: Solution
# submission_id: 8231152861c1bbe2281c1423be5144e5b9ded47a
# seed: 3269365175

# Time:  O(n * h)
# Space: O(h)

class Solution(object):
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        result, path = [], []
        self.binaryTreePathsRecu(root, path, result)
        return result

    def binaryTreePathsRecu(self, node, path, result):
        if node is None:
            return

        if node.left is node.right is None:
            ans = ""
            for n in path:
                ans += str(n.val) + "->"
            result.append(ans + str(node.val))

        if node.left:
            path.append(node)
            self.binaryTreePathsRecu(node.left, path, result)
            path.pop()

        if node.right:
            path.append(node)
            self.binaryTreePathsRecu(node.right, path, result)
            path.pop()