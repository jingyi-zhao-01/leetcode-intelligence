# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-complete-tree-nodes
# source_path: LeetCode-Solutions-master/Python/count-complete-tree-nodes.py
# solution_class: Solution2
# submission_id: 2e36960f4905a707ed27c50d90b6aa7408de7874
# seed: 3623639356

# Time:  O(h * h) = O((logn)^2)
# Space: O(1)

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        pass

class Solution2(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def check(node, n):
            base = 1
            while base <= n:
                base <<= 1
            base >>= 2

            while base:
                if (n & base) == 0:
                    node = node.left
                else:
                    node = node.right
                base >>= 1
            return bool(node)

        if not root:
            return 0

        node, level = root, 0
        while node.left:
            node = node.left
            level += 1

        left, right = 2**level, 2**(level+1)-1
        while left <= right:
            mid = left+(right-left)//2
            if not check(root, mid):
                right = mid-1
            else:
                left = mid+1
        return right