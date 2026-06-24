# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: count-nodes-equal-to-average-of-subtree
# source_path: LeetCode-Solutions-master/Python/count-nodes-equal-to-average-of-subtree.py
# solution_class: Solution
# submission_id: 4dfb41cb791e1dbc0bca7f09a0bac744396a4a62
# seed: 1876763371

# Time:  O(n)
# Space: O(h)

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        pass


# dfs

class Solution(object):
    def averageOfSubtree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def iter_dfs(root):
            result = 0
            stk = [(1, (root, [0]*2))]
            while stk:
                step, args = stk.pop()
                if step == 1:
                    node, ret = args
                    if not node:
                        continue
                    ret1, ret2 = [0]*2, [0]*2
                    stk.append((2, (node, ret1, ret2, ret)))
                    stk.append((1, (node.right, ret2)))
                    stk.append((1, (node.left, ret1)))
                elif step == 2:
                    node, ret1, ret2, ret = args
                    ret[0] = ret1[0]+ret2[0]+node.val
                    ret[1] = ret1[1]+ret2[1]+1
                    result += int(ret[0]//ret[1] == node.val)
            return result
        
        return iter_dfs(root)