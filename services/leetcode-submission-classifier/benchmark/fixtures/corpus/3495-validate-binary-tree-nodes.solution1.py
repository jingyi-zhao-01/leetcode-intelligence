# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: validate-binary-tree-nodes
# source_path: LeetCode-Solutions-master/Python/validate-binary-tree-nodes.py
# solution_class: Solution
# submission_id: 23381a51a1b2ee0481473a30738b53ef20c1a530
# seed: 3645487553

# Time:  O(n)
# Space: O(n)

class Solution(object):
    def validateBinaryTreeNodes(self, n, leftChild, rightChild):
        """
        :type n: int
        :type leftChild: List[int]
        :type rightChild: List[int]
        :rtype: bool
        """
        roots = set(range(n)) - set(leftChild) - set(rightChild)
        if len(roots) != 1:
            return False
        root, = roots
        stk = [root]
        lookup = set([root])
        while stk:
            node = stk.pop()
            for c in (leftChild[node], rightChild[node]):
                if c < 0:
                    continue
                if c in lookup:
                    return False
                lookup.add(c)
                stk.append(c)
        return len(lookup) == n