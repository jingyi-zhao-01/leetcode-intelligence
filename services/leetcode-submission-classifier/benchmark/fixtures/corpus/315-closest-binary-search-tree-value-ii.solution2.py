# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: closest-binary-search-tree-value-ii
# source_path: LeetCode-Solutions-master/Python/closest-binary-search-tree-value-ii.py
# solution_class: Solution2
# submission_id: f6168f5ed7811b4928c093b0d4a634acc7b97495
# seed: 3310179726

# Time:  O(h + k)
# Space: O(h)

class Solution2(object):
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        # Helper class to make a stack to the next node.
        class BSTIterator:
            # @param root, a binary search tree's root node
            def __init__(self, stack, child1, child2):
                self.stack = list(stack)
                self.cur = self.stack.pop()
                self.child1 = child1
                self.child2 = child2

            # @return an integer, the next node
            def next(self):
                node = None
                if self.cur and self.child1(self.cur):
                    self.stack.append(self.cur)
                    node = self.child1(self.cur)
                    while self.child2(node):
                        self.stack.append(node)
                        node = self.child2(node)
                elif self.stack:
                    prev = self.cur
                    node = self.stack.pop()
                    while node:
                        if self.child2(node) is prev:
                            break
                        else:
                            prev = node
                            node = self.stack.pop() if self.stack else None
                self.cur = node
                return node

        # Build the stack to the closet node.
        stack = []
        while root:
            stack.append(root)
            root = root.left if target < root.val else root.right
        dist = lambda node: abs(node.val - target) if node else float("inf")
        stack = stack[:stack.index(min(stack, key=dist))+1]

        # The forward or backward iterator.
        backward = lambda node: node.left
        forward = lambda node: node.right
        smaller_it, larger_it = BSTIterator(stack, backward, forward), BSTIterator(stack, forward, backward)
        smaller_node, larger_node = smaller_it.next(), larger_it.next()

        # Get the closest k values by advancing the iterators of the stacks.
        result = [stack[-1].val]
        for _ in xrange(k - 1):
            if dist(smaller_node) < dist(larger_node):
                result.append(smaller_node.val)
                smaller_node = smaller_it.next()
            else:
                result.append(larger_node.val)
                larger_node = larger_it.next()
        return result