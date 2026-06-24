# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: closest-binary-search-tree-value-ii
# source_path: LeetCode-Solutions-master/Python/closest-binary-search-tree-value-ii.py
# solution_class: Solution
# submission_id: 9dbe6778d635534b43f110336e52e893b8ecf78c
# seed: 28758236

# Time:  O(h + k)
# Space: O(h)

class Solution(object):
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        # Helper to make a stack to the next node.
        def nextNode(stack, child1, child2):
            if stack:
                if child2(stack):
                    stack.append(child2(stack))
                    while child1(stack):
                        stack.append(child1(stack))
                else:
                    child = stack.pop()
                    while stack and child is child2(stack):
                        child = stack.pop()

        # The forward or backward iterator.
        backward = lambda stack: stack[-1].left
        forward = lambda stack: stack[-1].right

        # Build the stack to the closest node.
        stack = []
        while root:
            stack.append(root)
            root = root.left if target < root.val else root.right
        dist = lambda node: abs(node.val - target)
        forward_stack = stack[:stack.index(min(stack, key=dist))+1]

        # Get the stack to the next smaller node.
        backward_stack = list(forward_stack)
        nextNode(backward_stack, backward, forward)

        # Get the closest k values by advancing the iterators of the stacks.
        result = []
        for _ in xrange(k):
            if forward_stack and \
                (not backward_stack or dist(forward_stack[-1]) < dist(backward_stack[-1])):
                result.append(forward_stack[-1].val)
                nextNode(forward_stack, forward, backward)
            elif backward_stack and \
                (not forward_stack or dist(backward_stack[-1]) <= dist(forward_stack[-1])):
                result.append(backward_stack[-1].val)
                nextNode(backward_stack, backward, forward)
        return result