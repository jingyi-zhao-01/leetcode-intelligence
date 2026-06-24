# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: verify-preorder-sequence-in-binary-search-tree
# source_path: LeetCode-Solutions-master/Python/verify-preorder-sequence-in-binary-search-tree.py
# solution_class: Solution
# submission_id: b854298b1002deebc8a752107ec1ae031d5bc196
# seed: 599766633

# Time:  O(n)
# Space: O(1)

class Solution(object):
    # @param {integer[]} preorder
    # @return {boolean}
    def verifyPreorder(self, preorder):
        low, i = float("-inf"), -1
        for p in preorder:
            if p < low:
                return False
            while i >= 0 and p > preorder[i]:
                low = preorder[i]
                i -= 1
            i += 1
            preorder[i] = p
        return True