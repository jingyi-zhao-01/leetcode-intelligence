# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-nodes-equal-to-sum-of-descendants
# source_path: LeetCode-Solutions-master/Python/count-nodes-equal-to-sum-of-descendants.py
# solution_class: Solution
# submission_id: 3198fc2e670acfaed9b002bd74b9187b15ab4638
# seed: 3741477035

# Time:  O(n)
# Space: O(h)

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        pass

class Solution(object):
    def equalToDescendants(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def iter_dfs(node):
            result = 0
            stk = [(1, [node, [0]])]
            while stk:
                step, args = stk.pop()
                if step == 1:
                    node, ret = args
                    if not node:
                        continue
                    ret1, ret2 = [0], [0]
                    stk.append((2, [node, ret1, ret2, ret]))
                    stk.append((1, [node.right, ret2]))
                    stk.append((1, [node.left, ret1]))
                elif step == 2:
                    node, ret1, ret2, ret = args
                    if node.val == ret1[0]+ret2[0]:
                        result += 1
                    ret[0] = ret1[0]+ret2[0]+node.val
            return result

        return iter_dfs(root)