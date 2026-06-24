# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: evaluate-boolean-binary-tree
# source_path: LeetCode-Solutions-master/Python/evaluate-boolean-binary-tree.py
# solution_class: Solution2
# submission_id: 44bc17bd7e5bd4abaca1724fb9288d41b468838a
# seed: 1347577479

# Time:  O(n)
# Space: O(h)

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        pass


# dfs with stack

class Solution2(object):
    def evaluateTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        INF = float("inf")
        OP = {
            2: lambda x, y: x or y,
            3: lambda x, y: x and y,
        }
        
        def dfs(node):
            if node.left == node.right:
                return node.val
            return OP[node.val](dfs(node.left), dfs(node.right))

        return dfs(root)