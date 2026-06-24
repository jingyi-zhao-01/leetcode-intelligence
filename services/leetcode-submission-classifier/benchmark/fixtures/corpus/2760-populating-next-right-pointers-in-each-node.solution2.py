# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: populating-next-right-pointers-in-each-node
# source_path: LeetCode-Solutions-master/Python/populating-next-right-pointers-in-each-node.py
# solution_class: Solution2
# submission_id: ba768913b0904f5a3f332bb10fdc5149a48477de
# seed: 305437336

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

class Solution2(object):
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        if root is None:
            return
        if root.left:
            root.left.next = root.right
        if root.right and root.next:
            root.right.next = root.next.left
        self.connect(root.left)
        self.connect(root.right)