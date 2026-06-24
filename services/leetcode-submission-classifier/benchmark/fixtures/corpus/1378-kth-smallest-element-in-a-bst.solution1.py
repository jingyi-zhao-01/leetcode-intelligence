# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: kth-smallest-element-in-a-bst
# source_path: LeetCode-Solutions-master/Python/kth-smallest-element-in-a-bst.py
# solution_class: Solution
# submission_id: f4704e9cb51153ca8b5e086870308a0e4ad2ead9
# seed: 79241904

# Time:  O(max(h, k))
# Space: O(h)

class Solution(object):
    # @param {TreeNode} root
    # @param {integer} k
    # @return {integer}
    def kthSmallest(self, root, k):
        s, cur, rank = [], root, 0

        while s or cur:
            if cur:
                s.append(cur)
                cur = cur.left
            else:
                cur = s.pop()
                rank += 1
                if rank == k:
                    return cur.val
                cur = cur.right

        return float("-inf")