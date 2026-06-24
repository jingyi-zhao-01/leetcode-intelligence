# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: evaluate-boolean-binary-tree
# source_path: LeetCode-Solutions-master/Python/evaluate-boolean-binary-tree.py
# solution_class: Solution
# submission_id: 360ba98f4d629daad74fadbc413119e775e22687
# seed: 2303541421

# Time:  O(n)
# Space: O(h)

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        pass


# dfs with stack

class Solution(object):
    def evaluateTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        INF = float("inf")
        OP = {
            2: lambda x, y: x or y,
            3: lambda x, y: x and y
        }
        
        def iter_dfs(root):
            ret = [0]
            stk = [(1, (root, ret))]
            while stk:
                step, args = stk.pop()
                if step == 1:
                    node, ret = args
                    if node.left == node.right:
                        ret[0] = node.val
                        continue
                    ret1, ret2 = [0], [0]
                    stk.append((2, (node, ret1, ret2, ret)))
                    stk.append((1, (node.right, ret2)))
                    stk.append((1, (node.left, ret1)))
                elif step == 2:
                    node, ret1, ret2, ret = args
                    ret[0] = OP[node.val](ret1[0], ret2[0])
            return ret[0]

        return iter_dfs(root)