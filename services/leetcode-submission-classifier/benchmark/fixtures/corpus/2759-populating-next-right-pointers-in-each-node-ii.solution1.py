# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: populating-next-right-pointers-in-each-node-ii
# source_path: LeetCode-Solutions-master/Python/populating-next-right-pointers-in-each-node-ii.py
# solution_class: Solution
# submission_id: a6f3f319c7d807afb28baf0f4db6fc77d85a3637
# seed: 3198445748

# Time:  O(n)
# Space: O(1)

# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution(object):
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        head = root
        pre = Node(0)
        cur = pre
        while root:
            while root:
                if root.left:
                    cur.next = root.left
                    cur = cur.next
                if root.right:
                    cur.next = root.right
                    cur = cur.next
                root = root.next
            root, cur = pre.next, pre
            cur.next = None
        return head