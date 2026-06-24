# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: linked-list-in-binary-tree
# source_path: LeetCode-Solutions-master/Python/linked-list-in-binary-tree.py
# solution_class: Solution2
# submission_id: d751dd315c88985d12cf2cd0b89a0185a02252ed
# seed: 3187165130

# Time:  O(n + l)
# Space: O(h + l)

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# kmp solution

class Solution2(object):
    def isSubPath(self, head, root):
        """
        :type head: ListNode
        :type root: TreeNode
        :rtype: bool
        """
        def dfs(head, root):
            if not head:
                return True
            if not root:
                return False
            return root.val == head.val and \
                   (dfs(head.next, root.left) or 
                    dfs(head.next, root.right))
    
        if not head:
            return True
        if not root:
            return False
        return dfs(head, root) or \
               self.isSubPath(head, root.left) or \
               self.isSubPath(head, root.right)