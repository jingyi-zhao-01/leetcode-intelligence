# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: all-elements-in-two-binary-search-trees
# source_path: LeetCode-Solutions-master/Python/all-elements-in-two-binary-search-trees.py
# solution_class: Solution
# submission_id: 0ee28fc78d726d4cea4dd977791c63232548933e
# seed: 3684698209

# Time:  O(n)
# Space: O(h)

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def getAllElements(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: List[int]
        """
        def inorder_gen(root):
            result, stack = [], [(root, False)]
            while stack:
                root, is_visited = stack.pop()
                if root is None:
                    continue
                if is_visited:
                    yield root.val
                else:
                    stack.append((root.right, False))
                    stack.append((root, True))
                    stack.append((root.left, False))
            yield None
        
        result = []
        left_gen, right_gen = inorder_gen(root1), inorder_gen(root2)
        left, right = next(left_gen), next(right_gen)
        while left is not None or right is not None:
            if right is None or (left is not None and left < right):
                result.append(left)
                left = next(left_gen)
            else:
                result.append(right)
                right = next(right_gen)
        return result