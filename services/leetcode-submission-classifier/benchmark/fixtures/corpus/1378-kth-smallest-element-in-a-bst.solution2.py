# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: kth-smallest-element-in-a-bst
# source_path: LeetCode-Solutions-master/Python/kth-smallest-element-in-a-bst.py
# solution_class: Solution2
# submission_id: c921966e250fb1de38ff554e1e6f875b8956cd74
# seed: 2600810812

# Time:  O(max(h, k))
# Space: O(h)

class Solution2(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        def gen_inorder(root):
            if root:
                for n in gen_inorder(root.left):
                    yield n

                yield root.val

                for n in gen_inorder(root.right):
                    yield n

        return next(islice(gen_inorder(root), k-1, k))