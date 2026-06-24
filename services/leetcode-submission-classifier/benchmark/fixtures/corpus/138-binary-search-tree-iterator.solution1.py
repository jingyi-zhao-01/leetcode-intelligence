# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: binary-search-tree-iterator
# source_path: LeetCode-Solutions-master/Python/binary-search-tree-iterator.py
# solution_class: Solution
# submission_id: 6fc1c050229e2d2c8f1a51fb4213d5de746a6bdd
# seed: 1988197793

# Time:  O(1)
# Space: O(h), h is height of binary tree

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BSTIterator(object):
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.__stk = []
        self.__traversalLeft(root)

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        return self.__stk

    # @return an integer, the next smallest number
    def next(self):
        node = self.__stk.pop()
        self.__traversalLeft(node.right)
        return node.val
    
    def __traversalLeft(self, node):
        while node is not None:
            self.__stk.append(node)
            node = node.left

