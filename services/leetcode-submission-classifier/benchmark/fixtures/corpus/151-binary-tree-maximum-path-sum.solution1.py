# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: binary-tree-maximum-path-sum
# source_path: LeetCode-Solutions-master/Python/binary-tree-maximum-path-sum.py
# solution_class: Solution
# submission_id: 86865b30377dd1ad59780d4415c9e731ac7a2f53
# seed: 3048665488

# Time:  O(n)
# Space: O(h), h is height of binary tree

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    # @param root, a tree node
    # @return an integer
    def maxPathSum(self, root):
        def iter_dfs(node):
            result = float("-inf")
            max_sum = [0]
            stk = [(1, [node, max_sum])]
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
                    result = max(result, node.val+max(ret1[0], 0)+max(ret2[0], 0))
                    ret[0] = node.val+max(ret1[0], ret2[0], 0)
            return result
        
        return iter_dfs(root)