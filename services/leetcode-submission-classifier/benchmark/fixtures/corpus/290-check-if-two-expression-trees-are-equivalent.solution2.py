# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: check-if-two-expression-trees-are-equivalent
# source_path: LeetCode-Solutions-master/Python/check-if-two-expression-trees-are-equivalent.py
# solution_class: Solution2
# submission_id: 5b8a8145f3717fdcce10355487590eba1dcb159d
# seed: 2938175272

# Time:  O(n)
# Space: O(1)

import collections
import functools


# Definition for a binary tree node.
class Node(object):
    def __init__(self, val=" ", left=None, right=None):
        pass


# morris traversal

class Solution2(object):
    def checkEquivalence(self, root1, root2):
        """
        :type root1: Node
        :type root2: Node
        :rtype: bool
        """
        def add_counter(counter, prev, d, val):
            if val.isalpha():
                counter[ord(val)-ord('a')] += d if prev[0] == '+' else -d
            prev[0] = val

        def inorder_traversal(root, cb):
            def traverseLeft(node, stk):
                while node:
                    stk.append(node)
                    node = node.left 

            stk = []
            traverseLeft(root, stk)
            while stk:
                curr = stk.pop()
                cb(curr.val)
                traverseLeft(curr.right, stk)
                
        counter = collections.defaultdict(int)
        inorder_traversal(root1, functools.partial(add_counter, counter, ['+'], 1))
        inorder_traversal(root2, functools.partial(add_counter, counter, ['+'], -1))
        return all(v == 0 for v in counter.itervalues())