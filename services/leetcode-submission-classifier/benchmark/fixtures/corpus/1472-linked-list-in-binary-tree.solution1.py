# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: linked-list-in-binary-tree
# source_path: LeetCode-Solutions-master/Python/linked-list-in-binary-tree.py
# solution_class: Solution
# submission_id: cee4fe2efacc420b5df0106b35472e5f3f64a64e
# seed: 3463456990

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

class Solution(object):
    def isSubPath(self, head, root):
        """
        :type head: ListNode
        :type root: TreeNode
        :rtype: bool
        """
        def getPrefix(head):
            pattern, prefix = [head.val], [-1]
            j = -1
            node = head.next
            while node:
                while j+1 and pattern[j+1] != node.val:
                    j = prefix[j]
                if pattern[j+1] == node.val:
                    j += 1
                pattern.append(node.val)
                prefix.append(j)
                node = node.next
            return pattern, prefix
            
        def dfs(pattern, prefix, root, j):
            if not root:
                return False
            while j+1 and pattern[j+1] != root.val:
                j = prefix[j]
            if pattern[j+1] == root.val:
                j += 1
            if j+1 == len(pattern):
                return True
            return dfs(pattern, prefix, root.left, j) or \
                   dfs(pattern, prefix, root.right, j)
        
        if not head:
            return True
        pattern, prefix = getPrefix(head)
        return dfs(pattern, prefix, root, -1)