# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: binary-tree-postorder-traversal
# source_path: LeetCode-Solutions-master/Python/binary-tree-postorder-traversal.py
# solution_class: Solution
# submission_id: 391f6998cb07c1e550a3e7fa7e4cb6e3451bcc41
# seed: 1379832765

# Time:  O(n)
# Space: O(1)

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Morris Traversal Solution

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        dummy = TreeNode(0)
        dummy.left = root
        result, cur = [], dummy
        while cur:
            if cur.left is None:
                cur = cur.right
            else:
                node = cur.left
                while node.right and node.right != cur:
                    node = node.right

                if node.right is None:
                    node.right = cur
                    cur = cur.left
                else:
                    result += self.traceBack(cur.left, node)
                    node.right = None
                    cur = cur.right

        return result

    def traceBack(self, frm, to):
        result, cur = [], frm
        while cur is not to:
            result.append(cur.val)
            cur = cur.right
        result.append(to.val)
        result.reverse()
        return result