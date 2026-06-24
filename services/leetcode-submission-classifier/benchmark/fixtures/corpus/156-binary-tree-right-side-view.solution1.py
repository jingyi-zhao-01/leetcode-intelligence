# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: binary-tree-right-side-view
# source_path: LeetCode-Solutions-master/Python/binary-tree-right-side-view.py
# solution_class: Solution
# submission_id: 1209fabc919a2ef82c249d6572e67b5f1bcd0d45
# seed: 3564462226

# Time:  O(n)
# Space: O(h)

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    # @param root, a tree node
    # @return a list of integers
    def rightSideView(self, root):
        result = []
        self.rightSideViewDFS(root, 1, result)
        return result

    def rightSideViewDFS(self, node, depth, result):
        if not node:
            return

        if depth > len(result):
            result.append(node.val)

        self.rightSideViewDFS(node.right, depth+1, result)
        self.rightSideViewDFS(node.left, depth+1, result)