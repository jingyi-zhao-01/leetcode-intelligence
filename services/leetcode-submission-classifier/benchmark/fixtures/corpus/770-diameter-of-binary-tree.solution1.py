# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: diameter-of-binary-tree
# source_path: LeetCode-Solutions-master/Python/diameter-of-binary-tree.py
# solution_class: Solution
# submission_id: 4fa355b0df7d74ca523fbd6ae6c334eaa7a3174d
# seed: 3287615676

# Time:  O(n)
# Space: O(h)

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def iter_dfs(node):
            result = 0
            stk = [(1, [node, [0]])]
            while stk:
                step, params = stk.pop()
                if step == 1:
                    node, ret = params
                    if not node:
                        continue
                    ret1, ret2 = [0], [0]
                    stk.append((2, [node, ret1, ret2, ret]))
                    stk.append((1, [node.right, ret2]))
                    stk.append((1, [node.left, ret1]))
                elif step == 2:
                    node, ret1, ret2, ret = params
                    result = max(result, ret1[0]+ret2[0])
                    ret[0] = 1+max(ret1[0], ret2[0])
            return result
        
        return iter_dfs(root)