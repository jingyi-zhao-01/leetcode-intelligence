# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: number-of-good-leaf-nodes-pairs
# source_path: LeetCode-Solutions-master/Python/number-of-good-leaf-nodes-pairs.py
# solution_class: Solution2
# submission_id: 56eb87c7a68f001e9517327ba3e7f7b24141b628
# seed: 3481691842

# Time:  O(n)
# Space: O(h)

import collections


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution2(object):
    def countPairs(self, root, distance):
        """
        :type root: TreeNode
        :type distance: int
        :rtype: int
        """
        def dfs(distance, node):
            if not node:
                return 0, collections.Counter()
            if not node.left and not node.right:
                return 0, collections.Counter([0])
            left, right = dfs(distance, node.left), dfs(distance, node.right)
            result = left[0]+right[0]
            for left_d, left_c in left[1].iteritems():
                for right_d,right_c in right[1].iteritems():
                    if left_d+right_d+2 <= distance:
                        result += left_c*right_c
            return result, collections.Counter({k+1:v for k,v in (left[1]+right[1]).iteritems()})
        
        return dfs(distance, root)[0]