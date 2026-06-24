# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: clone-binary-tree-with-random-pointer
# source_path: LeetCode-Solutions-master/Python/clone-binary-tree-with-random-pointer.py
# solution_class: Solution2
# submission_id: eeb8b1964b63261393f98d3ee184b4e424a8adb2
# seed: 3754642920

# Time:  O(n)
# Space: O(h)

# Definition for Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, random=None):
        self.val = val
        self.left = left
        self.right = right
        self.random = random


# Definition for NodeCopy.
class NodeCopy(object):
    def __init__(self, val=0, left=None, right=None, random=None):
        pass

class Solution2(object):
    def copyRandomBinaryTree(self, root):
        """
        :type root: Node
        :rtype: NodeCopy
        """ 
        lookup = collections.defaultdict(lambda: NodeCopy())
        lookup[None] = None
        stk = [root]
        while stk:
            node = stk.pop()
            if not node:
                continue
            lookup[node].val = node.val
            lookup[node].left = lookup[node.left]
            lookup[node].right = lookup[node.right]
            lookup[node].random = lookup[node.random]
            stk.append(node.right)
            stk.append(node.left)
        return lookup[root]