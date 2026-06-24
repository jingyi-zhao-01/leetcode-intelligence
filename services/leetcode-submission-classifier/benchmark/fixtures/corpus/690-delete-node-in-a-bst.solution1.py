# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: delete-node-in-a-bst
# source_path: LeetCode-Solutions-master/Python/delete-node-in-a-bst.py
# solution_class: Solution
# submission_id: c41c10c2ebdc6f849fe47ccb8334781951acc82d
# seed: 752032544

# Time:  O(h)
# Space: O(h)

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root:
            return root

        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                right = root.right
                del root
                return right
            elif not root.right:
                left = root.left
                del root
                return left
            else:
                successor = root.right
                while successor.left:
                    successor = successor.left

                root.val = successor.val
                root.right = self.deleteNode(root.right, successor.val)

        return root