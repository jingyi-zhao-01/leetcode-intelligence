# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: zigzag-level-sum-of-binary-tree
# source_path: LeetCode-Solutions-master/Python/zigzag-level-sum-of-binary-tree.py
# solution_class: Solution
# submission_id: aa2dfaafe820c3b8674adf64d0f0d062a1338381
# seed: 120966458

# Time:  O(n)
# Space: O(w)

# bfs

class Solution(object):
    def zigzagLevelSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        result = []
        q = [root]
        parity = 0
        while q:
            new_q = []
            total = 0
            stop = False
            for node in reversed(q):
                left, right = (node.left, node.right) if parity == 0 else (node.right, node.left)
                if left:
                    new_q.append(left)
                if right:
                    new_q.append(right)
                stop = stop or not left
                if not stop:
                    total += node.val
            result.append(total)
            q = new_q
            parity ^= 1
        return result