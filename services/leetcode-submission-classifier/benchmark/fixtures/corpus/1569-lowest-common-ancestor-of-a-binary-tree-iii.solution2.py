# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: lowest-common-ancestor-of-a-binary-tree-iii
# source_path: LeetCode-Solutions-master/Python/lowest-common-ancestor-of-a-binary-tree-iii.py
# solution_class: Solution2
# submission_id: 1ed5a3e402580b5bcd935c9fe32bb515caa3f05e
# seed: 3146053312

# Time:  O(h)
# Space: O(1)

# Definition for a Node.
class Node:
    def __init__(self, val):
        pass

class Solution2(object):
    def lowestCommonAncestor(self, p, q):
        """
        :type node: Node
        :rtype: Node
        """
        def depth(node):
            d = 0
            while node:
                node = node.parent
                d += 1
            return d
        
        p_d, q_d = depth(p), depth(q)
        while p_d > q_d:
            p = p.parent
            p_d -= 1
        while p_d < q_d:
            q = q.parent
            q_d -= 1
        while p != q:
            p = p.parent
            q = q.parent
        return p