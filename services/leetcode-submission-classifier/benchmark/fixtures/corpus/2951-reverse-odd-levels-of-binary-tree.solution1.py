# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: reverse-odd-levels-of-binary-tree
# source_path: LeetCode-Solutions-master/Python/reverse-odd-levels-of-binary-tree.py
# solution_class: Solution
# submission_id: 1f36b2bbbf594d9d49c577ee0303aa5383d1cc5f
# seed: 3325174594

# Time:  O(n)
# Space: O(n)

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        pass


# bfs

class Solution(object):
    def reverseOddLevels(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        q = [root]
        parity = 0
        while q:
            if parity:
                left, right = 0, len(q)-1
                while left < right:
                    q[left].val, q[right].val = q[right].val, q[left].val
                    left += 1
                    right -= 1
            if not q[0].left:
                break
            new_q = []
            for node in q:
                new_q.append(node.left)
                new_q.append(node.right)
            q = new_q       
            parity ^= 1
        return root