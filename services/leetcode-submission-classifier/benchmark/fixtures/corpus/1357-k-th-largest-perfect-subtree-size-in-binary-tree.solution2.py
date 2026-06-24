# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: k-th-largest-perfect-subtree-size-in-binary-tree
# source_path: LeetCode-Solutions-master/Python/k-th-largest-perfect-subtree-size-in-binary-tree.py
# solution_class: Solution2
# submission_id: e822c2e862ac0fd5239b03ae275c1c5a115348c8
# seed: 828548948

# Time:  O(n)
# Space: O(n)

import random


# iterative dfs, quick select

class Solution2(object):
    def kthLargestPerfectSubtree(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        def nth_element(nums, left, n, right, compare=lambda a, b: a < b):
            def tri_partition(nums, left, right, target):
                i = left
                while i <= right:
                    if compare(nums[i], target):
                        nums[i], nums[left] = nums[left], nums[i]
                        left += 1
                        i += 1
                    elif compare(target, nums[i]):
                        nums[i], nums[right] = nums[right], nums[i]
                        right -= 1
                    else:
                        i += 1
                return left, right

            while left <= right:
                pivot_idx = random.randint(left, right)
                pivot_left, pivot_right = tri_partition(nums, left, right, nums[pivot_idx])
                if pivot_left <= n <= pivot_right:
                    return
                elif pivot_left > n:
                    right = pivot_left-1
                else:  # pivot_right < n.
                    left = pivot_right+1

        def dfs(curr):
            if not curr:
                result.append(0)
                return
            dfs(curr.left)
            left = result[-1]
            dfs(curr.right)
            right = result[-1]
            result.append(left+right+1 if left == right != -1 else -1)

        result = []
        dfs(root)
        nth_element(result, 0, k-1, len(result)-1, lambda a, b: a > b)
        return result[k-1] if k-1 < len(result) and result[k-1] > 0 else -1