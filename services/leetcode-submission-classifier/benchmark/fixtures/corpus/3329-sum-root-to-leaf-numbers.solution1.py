# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: sum-root-to-leaf-numbers
# source_path: LeetCode-Solutions-master/Python/sum-root-to-leaf-numbers.py
# solution_class: Solution
# submission_id: 5c42c8d8873fba9cd57d39a70468157b75389373
# seed: 1549562254

# Time:  O(n)
# Space: O(h), h is height of binary tree

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    # @param root, a tree node
    # @return an integer
    def sumNumbers(self, root):
        return self.sumNumbersRecu(root, 0)

    def sumNumbersRecu(self, root, num):
        if root is None:
            return 0

        if root.left is None and root.right is None:
            return num * 10 + root.val

        return self.sumNumbersRecu(root.left, num * 10 + root.val) + self.sumNumbersRecu(root.right, num * 10 + root.val)