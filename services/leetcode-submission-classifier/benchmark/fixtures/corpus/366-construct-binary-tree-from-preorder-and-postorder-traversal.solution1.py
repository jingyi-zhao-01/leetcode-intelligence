# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: construct-binary-tree-from-preorder-and-postorder-traversal
# source_path: LeetCode-Solutions-master/Python/construct-binary-tree-from-preorder-and-postorder-traversal.py
# solution_class: Solution
# submission_id: 8c856fbb5e37fef120a719f6a164627fed396056
# seed: 3443447754

# Time:  O(n)
# Space: O(h)

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def constructFromPrePost(self, pre, post):
        """
        :type pre: List[int]
        :type post: List[int]
        :rtype: TreeNode
        """
        stack = [TreeNode(pre[0])]
        j = 0
        for i in xrange(1, len(pre)):
            node = TreeNode(pre[i])
            while stack[-1].val == post[j]:
                stack.pop()
                j += 1
            if not stack[-1].left:
                stack[-1].left = node
            else:
                stack[-1].right = node
            stack.append(node)
        return stack[0]