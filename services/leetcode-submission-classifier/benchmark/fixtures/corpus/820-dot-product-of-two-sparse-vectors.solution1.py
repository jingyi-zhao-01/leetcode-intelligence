# Source: https://github.com/kamyu104/LeetCode-Solutions
# problem_id: dot-product-of-two-sparse-vectors
# source_path: LeetCode-Solutions-master/Python/dot-product-of-two-sparse-vectors.py
# solution_class: Solution
# submission_id: 2fb11fab5f1a31e927aec2a9e9e228771736698f
# seed: 1555030333

# Time:  ctor: O(n)
#        dot_product: O(min(n, m))
# Space: O(n)

class SparseVector:
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.lookup = {i:v for i, v in enumerate(nums) if v}

    def dotProduct(self, vec):
        """
        :type vec: 'SparseVector'
        :rtype: int
        """
        if len(self.lookup) > len(vec.lookup):
            self, vec = vec, self
        return sum(v*vec.lookup[i] for i, v in self.lookup.iteritems() if i in vec.lookup)
