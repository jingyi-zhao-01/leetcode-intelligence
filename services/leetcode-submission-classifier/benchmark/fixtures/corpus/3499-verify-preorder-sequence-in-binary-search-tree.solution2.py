# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: verify-preorder-sequence-in-binary-search-tree
# source_path: LeetCode-Solutions-master/Python/verify-preorder-sequence-in-binary-search-tree.py
# solution_class: Solution2
# submission_id: e2719508cb4025fb1af140f88f620668e0d49ca5
# seed: 944092550

# Time:  O(n)
# Space: O(1)

class Solution2(object):
    # @param {integer[]} preorder
    # @return {boolean}
    def verifyPreorder(self, preorder):
        low = float("-inf")
        path = []
        for p in preorder:
            if p < low:
                return False
            while path and p > path[-1]:
                low = path[-1]
                path.pop()
            path.append(p)
        return True