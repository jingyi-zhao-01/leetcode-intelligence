# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: populating-next-right-pointers-in-each-node
# source_path: LeetCode-Solutions-master/Python/populating-next-right-pointers-in-each-node.py
# solution_class: Solution
# submission_id: ba441ca24d125be036f8f46175c32a87077c40bb
# seed: 508869708

# Time:  O(n)
# Space: O(1)

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

    def __repr__(self):
        if self is None:
            return "Nil"
        else:
            return "{} -> {}".format(self.val, repr(self.next))

class Solution(object):
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        head = root
        while head:
            cur = head
            while cur and cur.left:
                cur.left.next = cur.right
                if cur.next:
                    cur.right.next = cur.next.left
                cur = cur.next
            head = head.left