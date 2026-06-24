# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: convert-sorted-array-to-binary-search-tree
# source_path: LeetCode-Solutions-master/Python/convert-sorted-array-to-binary-search-tree.py
# solution_class: Solution2
# submission_id: ac561ce2b00e2470fac3819ae80f1b3c3a790128
# seed: 42025926

# Time:  O(n)
# Space: O(logn)

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution2(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        self.iterator = iter(nums)
        return self.helper(0, len(nums))
    
    def helper(self, start, end):
        if start == end:
            return None
        
        mid = (start + end) // 2
        left = self.helper(start, mid)
        current = TreeNode(next(self.iterator))
        current.left = left
        current.right = self.helper(mid+1, end)
        return current