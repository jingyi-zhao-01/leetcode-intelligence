# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: convert-sorted-array-to-binary-search-tree
# source_path: LeetCode-Solutions-master/Python/convert-sorted-array-to-binary-search-tree.py
# solution_class: Solution
# submission_id: 36cb8e249b8bd927424d3f430eacc4e06fdb16d4
# seed: 2143139943

# Time:  O(n)
# Space: O(logn)

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.sortedArrayToBSTRecu(nums, 0, len(nums))

    def sortedArrayToBSTRecu(self, nums, start, end):
        if start == end:
            return None
        mid = start + self.perfect_tree_pivot(end - start)
        node = TreeNode(nums[mid])
        node.left = self.sortedArrayToBSTRecu(nums, start, mid)
        node.right = self.sortedArrayToBSTRecu(nums, mid + 1, end)
        return node

    def perfect_tree_pivot(self, n):
        """
        Find the point to partition n keys for a perfect binary search tree
        """
        x = 1
        # find a power of 2 <= n//2
        # while x <= n//2:  # this loop could probably be written more elegantly :)
        #     x *= 2
        x = 1 << (n.bit_length() - 1)  # use the left bit shift, same as multiplying x by 2**n-1

        if x // 2 - 1 <= (n - x):
            return x - 1  # case 1: the left subtree of the root is perfect and the right subtree has less nodes
        else:
            return n - x // 2  # case 2 == n - (x//2 - 1) - 1 : the left subtree of the root