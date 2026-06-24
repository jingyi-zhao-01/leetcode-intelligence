# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: lowest-common-ancestor-of-a-binary-tree-iv
# source_path: LeetCode-Solutions-master/Python/lowest-common-ancestor-of-a-binary-tree-iv.py
# solution_class: Solution
# submission_id: 4346263edadf82b6610cd435bdb889c6613868a6
# seed: 1030116288

# Time:  O(n)
# Space: O(h)

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        pass

class Solution(object):
    def lowestCommonAncestor(self, root, nodes):
        """
        :type root: TreeNode
        :type nodes: List[TreeNode]
        """
        def iter_dfs(root, lookup):
            result = [0]
            stk = [(1, (root, result))]
            while stk:
                step, args = stk.pop()
                if step == 1:
                    node, ret = args
                    if not node or node in lookup:
                        ret[0] = node
                        continue
                    ret1, ret2 = [None], [None]
                    stk.append((2, (node, ret1, ret2, ret)))
                    stk.append((1, (node.right, ret2)))
                    stk.append((1, (node.left, ret1)))
                elif step == 2:
                    node, ret1, ret2, ret = args
                    if ret1[0] and ret2[0]:
                        ret[0] = node
                    else:
                        ret[0] = ret1[0] or ret2[0]
            return result[0]
        
        return iter_dfs(root, set(nodes))